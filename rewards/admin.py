from django.contrib import admin

from .models import RewardLog, ScheduledReward


@admin.register(ScheduledReward)
class ScheduledRewardAdmin(admin.ModelAdmin):
    list_display = ("user", "amount", "execute_at")
    list_filter = ("execute_at", "user")
    search_fields = ("user__username",)


@admin.register(RewardLog)
class RewardLogAdmin(admin.ModelAdmin):
    list_display = ("user", "amount", "given_at")
    list_filter = ("given_at", "user")
    search_fields = ("user__username",)
