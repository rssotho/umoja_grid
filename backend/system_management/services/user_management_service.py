import json

from rest_framework import status
from rest_framework.response import Response

from django.utils import timezone
from django.contrib.auth import (
    login,
    logout,
    authenticate
)

from system_management.packages.user_management_package import UserManagementPackage
from system_management.serializer.base_serializer import (
    LoginSerializer,
    UserSignUpSerializer,
)

class UserManagementService():

    def __init__(
        self,
        request = None
    ) -> None:

        self.request = request

    def user_sign_up(self):

        data = self.request.data

        serializer = UserSignUpSerializer(data = data)

        if not serializer.is_valid():

            response_data = json.dumps({
                'status': 'error',
                'message': 'Invalid data provided',
                'data': serializer.errors
            })
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        validated_data = serializer.validated_data
        email = validated_data.get('email')
        password = validated_data.get('password')
        last_name = validated_data.get('last_name')
        first_name = validated_data.get('first_name')
        phone_number = validated_data.get('phone_number')

        try:

            user_obj = UserManagementPackage().create_obj(
                email = email,
                password = password,
                last_name = last_name,
                first_name = first_name,
                phone_number = phone_number,
            )

            if not user_obj:

                response_data = json.dumps({
                    'status': 'error',
                    'message': 'Failed to onboard the user'
                })
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        except ValueError as message:

            response_data = json.dumps({
                'status': 'error',
                'message': str(message)
                })
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        except Exception as message:

            response_data = {
                'status': 'error',
                'message': str(message)
                }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        response_data = {
            'status': 'success',
            'message': 'User registered successfully'
        }
        return Response(response_data, status=status.HTTP_201_CREATED)

    def user_login(self):

        data = self.request.data
        serializer = LoginSerializer(data = data)

        if not serializer.is_valid():

            response_data = json.dumps({
                'status': 'error',
                'message': 'Invalid request to API',
                'data': serializer.errors
            })
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        validated_data: dict = serializer.validated_data
        email: str = validated_data.get('email')
        password: str = validated_data.get('password')

        try:

            user = authenticate(
                self.request,
                email = email,
                password = password,
            )

            

            if user is None:

                response_data = {
                    'status': 'error',
                    'message': 'Invalid credentials, please enter the correct details'
                }
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

            if not user.is_active:
                response_data = {
                    'status': 'error',
                    'message': 'Account is disabled'
                }
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

            login(self.request, user)

            user.last_login = timezone.now()
            user.save(update_fields=['last_login'])

            token = UserManagementPackage().create_token(user)

            user_details = {
                'user_id': user.id,
                'email': user.email,
                'role': user.role.role,
                'last_name': user.last_name,
                'first_name': user.first_name,
                'phone_number': user.phone_number,
            }

            response_data = {
                'status': 'success',
                'message': 'User logged in successfully',
                'data': {
                    'token': token.key,
                    'user_details': user_details,
                }
            }
            return Response(response_data, status=status.HTTP_200_OK)

        except ValueError as message:

            response_data = {
                'status': 'error',
                'message': str(message),
                'data': None
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        except Exception as message:

            response_data = {
                'status': 'error',
                'message': str(message),
                'data': None
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
