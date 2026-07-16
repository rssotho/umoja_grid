from system_management.models import (
    User
)
from global_app.package_helper import PackageHelper

from rest_framework.authtoken.models import Token


class UserManagementPackage(PackageHelper):

    def __init__(self) -> None:

        super().__init__(
            model = User,
            model_serializer = None
        )

    def create_token(self, user: User) -> Token:

        token, _ = Token.objects.get_or_create(
            user = user
        )

        if token is None:

            raise ValueError('The requesting user does not have the token')

        return token