from rest_framework import serializers

from news.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"  # 실 서비스에는 비추