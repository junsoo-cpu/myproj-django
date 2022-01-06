from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shop.views import ReviewViewSet


app_name = "shop"

router = DefaultRouter()
router.register("reviews", ReviewViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]