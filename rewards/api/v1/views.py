from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rewards.api.v1.serializers import RewardLogSerializer
from rewards.api.v1.services import can_request_reward_today, schedule_daily_reward
from rewards.models import RewardLog


class RewardListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        rewards = RewardLog.objects.filter(user=request.user).order_by("-given_at")
        serializer = RewardLogSerializer(rewards, many=True)
        return Response(serializer.data)


class RequestRewardView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        if not can_request_reward_today(user):
            return Response(
                {"detail": "You can only request a reward once per day."}, status=400
            )

        try:
            schedule_daily_reward(user)
        except ValueError as e:
            return Response({"detail": str(e)}, status=400)

        return Response(
            {"detail": "Reward successfully scheduled to be given in 5 minutes."},
            status=201,
        )
