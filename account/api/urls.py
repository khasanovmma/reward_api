from django.urls import include, path

urlpatterns = [
    path(
        "v1/account/",
        include(("account.api.v1.urls", "account"), namespace="account"),
    ),
]
