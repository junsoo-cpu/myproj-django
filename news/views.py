import json
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from news.models import Article
from news.serializers import ArticleSerializer
from django.http import HttpResponse


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


article_list = ListAPIView.as_view(
    queryset=Article.objects.all(),
    serializer_class=ArticleSerializer,
)

# # step 1
# def article_list(request):
#     qs = Article.objects.all()
#
#     # step 2
#     serializer = ArticleSerializer(qs, many=True)
#     data = serializer.data
#     # data = [
#     #     {
#     #         "id": article.id,
#     #         "title": article.title,
#     #         "content": article.content,
#     #         "photo": request.build_absolute_uri(article.photo.url) if article.photo else None,
#     #     }
#     #     for article in qs
#     # ]
#     json_string = json.dumps(data)
#     return HttpResponse(json_string)
