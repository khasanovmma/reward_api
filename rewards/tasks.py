from celery import shared_task
from django.utils import timezone

from rewards.models import RewardLog, ScheduledReward


@shared_task(bind=True, max_retries=3)
def process_scheduled_reward(self, reward_id):
    try:
        reward = ScheduledReward.objects.get(id=reward_id)
        if reward.execute_at <= timezone.now():
            user = reward.user
            user.coins += reward.amount
            user.save()

            RewardLog.objects.create(user=user, amount=reward.amount)

            reward.delete()
    except ScheduledReward.DoesNotExist:
        self.retry(countdown=5)
