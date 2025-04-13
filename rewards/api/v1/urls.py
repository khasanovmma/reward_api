from django.urls import path

from rewards.api.v1.views import RequestRewardView, RewardListView

app_name = "rewards"

urlpatterns = [
    path("rewards/", RewardListView.as_view(), name="reward-list"),
    path("rewards/request/", RequestRewardView.as_view(), name="reward-request"),
]
