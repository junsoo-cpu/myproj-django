import re

from rest_framework import serializers

from animation.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"  # 실 서비스에는 비추

    def validate_name(self, name):
        if len(name) < 2:
            raise serializers.ValidationError("2글자 이상!!")
        if not re.search(r"[ㄱ-힣]", name):
            raise serializers.ValidationError("한글을 써주세요.")
        return name
