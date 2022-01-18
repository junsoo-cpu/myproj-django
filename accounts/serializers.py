from typing import Dict

from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as OrigTokenObtainPairSerializer,
    TokenRefreshSerializer as OrigTokenRefreshSerializer,
)


class TokenObtainPairSerializer(OrigTokenObtainPairSerializer):

    # JMT playload 커스텀
    # @classmethod
    # def get_token(cls, user) -> Dict:
    #     token = super().get_token(user)
    #     token['username'] = user.username
    #     token['first_name'] = user.first_name
    #     token['last_name'] = user.last_name
    #     return token

    # access/refresh 속성 외 추가
    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        data['first_name'] = self.user.first_name
        data['last_name'] = self.user.last_name


class TokenRefreshSerializer(OrigTokenRefreshSerializer):
    pass