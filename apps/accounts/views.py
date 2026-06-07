from rest_framework import status
from rest_framework.views import APIView

from apps.accounts.serializers import (
    LoginSerializer,
    UserSerializer,
)
from apps.accounts.services import AuthService
from core.responses import success_response


class LoginView(APIView):

    def post(self, request):

        serializer = LoginSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        user = serializer.validated_data["user"]

        tokens = AuthService.generate_tokens(
            user
        )

        user_data = UserSerializer(
            user
        ).data

        return success_response(
            data={
                "user": user_data,
                "tokens": tokens,
            },
            message="Login successful.",
            status_code=status.HTTP_200_OK
        )