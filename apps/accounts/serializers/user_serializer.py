from rest_framework import serializers
from django.contrib.auth import authenticate
from apps.accounts.models import User
    
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

