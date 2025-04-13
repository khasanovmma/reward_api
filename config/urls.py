from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("account.api.urls")),
    path("api/", include("rewards.api.urls")),
]
