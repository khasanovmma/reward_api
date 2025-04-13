from django.urls import include, path

urlpatterns = [
    path(
        "v1/rewards/",
        include(("rewards.api.v1.urls", "rewards"), namespace="rewards"),
    ),
]
