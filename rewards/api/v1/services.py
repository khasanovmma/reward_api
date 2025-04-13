from datetime import timedelta

from django.utils import timezone

from rewards.models import ScheduledReward


def can_request_reward_today(user):
    now = timezone.now()
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    return not ScheduledReward.objects.filter(
        user=user, created_at__gte=start_of_day
    ).exists()


def schedule_daily_reward(user, delay_minutes=5, amount=10):
    now = timezone.now()
    execute_at = now + timedelta(minutes=delay_minutes)

    time_window = timedelta(minutes=2)
    duplicate_exists = ScheduledReward.objects.filter(
        user=user, execute_at__range=(execute_at - time_window, execute_at + time_window)
    ).exists()

    if duplicate_exists:
        raise ValueError("Reward already scheduled in this time window.")

    return ScheduledReward.objects.create(user=user, amount=amount, execute_at=execute_at)
