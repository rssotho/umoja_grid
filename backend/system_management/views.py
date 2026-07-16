from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.permissions import AllowAny

from global_app import constants as constant
from global_app.roles_required import roles_required

from system_management.services.user_management_service import UserManagementService


@api_view(['POST'])
@authentication_classes([])
@permission_classes([AllowAny])
def user_sign_up(request):

    response = UserManagementService(
        request = request
    ).user_sign_up()

    return response


@api_view(['POST'])
@authentication_classes([])
@permission_classes([AllowAny])
def user_login(request):

    response = UserManagementService(
        request = request
    ).user_login()

    return response