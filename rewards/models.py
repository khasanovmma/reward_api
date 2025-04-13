from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class ScheduledReward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    execute_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reward {self.amount} - {self.user} - {self.execute_at}"


class RewardLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    given_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount} - {self.user} - {self.given_at}"
