from django.urls import path, include
from rest_framework.routers import DefaultRouter

from news import views
from news.views import ArticleViewSet

app_name = "news"

router = DefaultRouter()
router.register("articles", ArticleViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("articles.json", views.article_list),
]
