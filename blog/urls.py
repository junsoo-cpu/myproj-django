from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog import views
from blog.views import PostViewSet

app_name = "blog"

router = DefaultRouter()
router.register("posts", PostViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("post.json", views.post_list),
]
