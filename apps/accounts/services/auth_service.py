from rest_framework_simplejwt.tokens import RefreshToken


class AuthService:

    @staticmethod
    def generate_tokens(user):

        refresh = RefreshToken.for_user(user)

        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }
    
    
    @staticmethod
    def change_password(
        user,
        current_password,
        new_password
    ):
        
        if not user.check_password(
            current_password
        ):
            raise ValueError(
                "Current password is incorrect."
            )
        
        user.set_password(
            new_password
        )

        user.save()

        return user