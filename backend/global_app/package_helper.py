from django.db.models import (
    Model,
    QuerySet
)
from django.db import(
    transaction,
    IntegrityError
)
from django.core.exceptions import ObjectDoesNotExist

from typing import(
    Any,
    Dict,
    List,
    Union,
    Optional,
)


class PackageHelper:
    """
    Utility for basic CRUD + serialization on a single Django model.
    """

    def __init__(
        self,
        model: Model,
        model_serializer: Any
    ) -> None:
        """
        :param model: the Django model class
        :param model_serializer: DRF Serializer for that model
        """
        self.model = model
        self.serializer = model_serializer

    def create_obj(self, data: Dict[str, Any]) -> Model:
        """
        Create and return a new model instance.
        """
        try:
            return self.model.objects.create(**data)
        except Exception:
            return None

    def get_obj(self, **filters) -> Optional[Model]:
        """
        Return a single instance matching filters, or None.
        """
        try:
            return self.model.objects.get(**filters)
        except (self.model.DoesNotExist, self.model.MultipleObjectsReturned):
            return None

    def list_objs(
        self,
        filters: Dict[str, Any] =   None
    ) -> QuerySet:
        """
        Return a QuerySet of instances, filtered if filters provided.
        """
        qs = self.model.objects.all()
        return qs if not filters else qs.filter(**filters)

    def filter_by_q_condition(
        self,
        q_condition
    ) -> QuerySet:
        return self.model.objects.filter(
            q_condition
        )

    def update_obj(self, obj_id: int, data: Dict[str, Any]) -> Model:
        """
        Update a single instance by id with data dict.
        """
        if not data:
            raise ValueError("No update data provided")
        try:
            inst = self.model.objects.get(id=obj_id)
        except self.model.DoesNotExist:
            raise ObjectDoesNotExist(f"{self.model.__name__}({obj_id}) not found")
        for k, v in data.items():
            setattr(inst, k, v)
        try:
            inst.save()
        except IntegrityError as e:
            raise IntegrityError(f"Failed to update {self.model.__name__}: {e}")
        return inst

    def delete_obj(self, obj_id: int) -> None:
        """
        Delete a single instance by id.
        """
        try:
            inst = self.model.objects.get(id=obj_id)
        except self.model.DoesNotExist:
            raise ObjectDoesNotExist(
                f"{self.model.__name__}({obj_id}) not found"
            )
        inst.delete()

    def serialize(
        self,
        objs: Union[Model, List[Model]],
        context: Optional[Dict[str, Any]] = None
    ) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        """
        Serialize one instance or list of instances using self.serializer.
        """

        if isinstance(objs, QuerySet):
            objs = list(objs)

        many = isinstance(objs, list)
        serializer = self.serializer(
            objs,
            many=many,
            context=context
        )
        return serializer.data

    def bulk_create_objs(
        self,
        objs_data: List[Dict[str, Any]],
        batch_size: Optional[int] = None,
        ignore_conflicts: bool = False
    ) -> List[Model]:
        """
        Efficiently bulk create multiple instances, all inside a single atomic block.
        """
        if not objs_data:
            return []

        instances = [
            self.model(**data)
            for data in objs_data
        ]

        try:
            with transaction.atomic():
                # If batch_size is None it's one INSERT, otherwise N batched INSERTs.
                return self.model.objects.bulk_create(
                    instances,
                    batch_size=batch_size,
                    ignore_conflicts=ignore_conflicts
                )
        except IntegrityError as e:
            raise IntegrityError(f"Failed to bulk create {self.model.__name__}: {e}")

    def update_or_create_obj(
        self,
        filters: Dict[str, Any],
        defaults: Dict[str, Any]
    ) -> Model:
        """
        Update an existing instance or create a new one if it doesn't exist.
        """
        try:
            obj,_ = self.model.objects.update_or_create(
                defaults=defaults,
                **filters
            )
            return obj
        except IntegrityError as e:
            raise IntegrityError(f"Failed to update or create {self.model.__name__}: {e}")