from rest_framework import serializers

class UserSignUpSerializer (serializers.Serializer):

    email = serializers.CharField()
    password = serializers.CharField()
    last_name = serializers.CharField()
    first_name = serializers.CharField()
    phone_number = serializers.CharField()

class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)