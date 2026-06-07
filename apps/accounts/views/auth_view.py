from rest_framework import status
from rest_framework.views import APIView

from apps.accounts.serializers import (
    LoginSerializer,
    UserSerializer,
    ChangePasswordSerializer,
)
from apps.accounts.services import AuthService
from core.responses import success_response, error_response
from rest_framework.permissions import IsAuthenticated


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


class CurrentUserView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        user_data = UserSerializer(
            request.user
        ).data

        return success_response(
            data=user_data,
            message="User profile fetched successfully."
        )
    
class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = (
            ChangePasswordSerializer(
                data=request.data
            )
        )

        serializer.is_valid(
            raise_exception=True
        )

        try:
            AuthService.change_password(
                user=request.user,
                current_password=serializer.validated_data[
                    "current_password"
                ],
                new_password=serializer.validated_data[
                    "new_password"
                ]
            )

            return success_response(
                message="Password changed successfully."
            )
        
        except ValueError as error:

            return error_response(
                message=str(error),
                status_code=400
            )