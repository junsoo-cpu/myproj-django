from rest_framework.viewsets import ModelViewSet
from news.models import Article
from news.serializers import ArticleSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer