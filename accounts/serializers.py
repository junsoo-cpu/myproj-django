from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as OrigTokenObtainPairSerializer,
    TokenRefreshSerializer as OrigTokenRefreshSerializer,
)


User = get_user_model()


class UserCreationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["username", "password", "password2"]

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError("동일한 암호를 지정해주세요.")
        return attrs

    def create(self, validated_data):
        # 리턴 : 생성된 User 모델 인스턴스
        username = validated_data["username"]
        password = validated_data["password"]

        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()

        return new_user


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
        data["username"] = self.user.username
        data["first_name"] = self.user.first_name
        data["last_name"] = self.user.last_name
        # TODO: 프로필 이미지 URL
        return data


class TokenRefreshSerializer(OrigTokenRefreshSerializer):
    pass