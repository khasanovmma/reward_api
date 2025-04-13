from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from rewards.models import ScheduledReward
from rewards.tasks import process_scheduled_reward


@receiver(post_save, sender=ScheduledReward)
def schedule_reward_task(sender, instance, created, **kwargs):
    if created:
        delay = (instance.execute_at - timezone.now()).total_seconds()
        process_scheduled_reward.apply_async((instance.id,), countdown=delay)
