from rest_framework import status
from rest_framework.response import Response

class StatusHelper:

    @staticmethod
    def success(message: str, status_code: int = status.HTTP_200_OK, data=None) -> Response:

        response_data = {
            'status': 'success',
            'message': message
        }

        if data is not None:

            response_data['data'] = data
        return Response(response_data, status=status_code)

    @staticmethod
    def error(message: str, data=None) -> Response:

        response_data = {
            'status': 'error',
            'message': message
        }

        if data is not None:

            response_data['data'] = data
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)