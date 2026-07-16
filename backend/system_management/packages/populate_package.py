from global_app.package_helper import PackageHelper

from system_management.models import (
    Role,
    Race,
    Title,
    Gender,
    Province
)
from system_management.serializer.model_serializer import (
    ViewRoleModelSerializer,
    ViewRaceModelSerializer,
    ViewTitleModelSerializer,
    ViewGenderModelSerializer,
    ViewProvinceModelSerializer
)


class PopulateRolePackage(PackageHelper):

    def __init__(self) -> None:

        super().__init__(
            model = Role,
            model_serializer = ViewRoleModelSerializer
        )

class PopulateRacePackage(PackageHelper):

    def __init__(self) -> None:

        super().__init__(
            model = Race,
            model_serializer = ViewRaceModelSerializer
        )

class PopulateTitlePackage(PackageHelper):

    def __init__(self) -> None:

        super().__init__(
            model = Title,
            model_serializer = ViewTitleModelSerializer
        )

class PopulateGenderPackage(PackageHelper):

    def __init__(self) -> None:

        super().__init__(
            model = Gender,
            model_serializer = ViewGenderModelSerializer
        )

class PopulateProvincePackage(PackageHelper):

    def __init__(self) -> None:

        super().__init__(
            model = Province,
            model_serializer = ViewProvinceModelSerializer
        )

