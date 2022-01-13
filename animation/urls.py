from django.urls import path, include
from rest_framework.routers import DefaultRouter

from animation import views
from animation.views import ProfileViewSet

app_name = "animation"

router = DefaultRouter()
router.register("profile", ProfileViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("profile.json", views.profile_list),
]