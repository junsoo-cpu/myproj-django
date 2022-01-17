from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("shop/", include("shop.urls")),
    path("blog/", include("blog.urls")),
    path("news/", include("news.urls")),
    path("animation/", include("animation.urls")),
    path("accounts/", include("accounts.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Todo : 아래 token view는 accounts 앱 내에 두는 것이 맞다.

