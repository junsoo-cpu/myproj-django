from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.views import PostViewSet

app_name = "blog"

router = DefaultRouter()
router.register("posts", PostViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)