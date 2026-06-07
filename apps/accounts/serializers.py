from rest_framework import serializers
from django.contrib.auth import authenticate
from apps.accounts.models import User

class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField()

    password = serializers.CharField(
        write_only = True
    )

    def validate(self, attrs):
        email =attrs.get("email")
        password = attrs.get("password")

        user = authenticate(
            username=email,
            password=password
        )

        if not user:
            raise serializers.ValidationError(
                "Invalid credentials."
            )
        
        attrs["user"] = user

        return attrs
    

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = (
            "id",
            "employee_id",
            "email",
            "first_name",
            "last_name",
            "role",
        )

        