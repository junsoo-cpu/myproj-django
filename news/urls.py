from django.urls import path, include
from rest_framework.routers import DefaultRouter
from news import views


app_name = "news"

router = DefaultRouter()
router.register("articles", views.ArticleViewSet)

urlpatterns = [
    # path("articles.json", views.article_list),
    path("api/", include(router.urls)),
]