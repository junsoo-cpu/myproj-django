from rest_framework_simplejwt.views import (
    TokenObtainPairView as OrigTokenObtainPairView,
    TokenRefreshView as OrigTokenRefreshView,
)
from accounts.serializers import TokenObtainPairSerializer


class TokenObtainPairView (OrigTokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class TokenRefreshView(OrigTokenRefreshView):
    pass