from django.contrib.auth import get_user_model
from django.conf import settings
import uuid
from django.db import models

# Create your models here.


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


# weekly, monthly, yearly
class GoalFrequency(models.Model):
    goal_freq_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    goalFrequency = models.CharField(max_length=200)

    def __str__(self):
        return str(self.goalFrequency)


# 15 mins, 30 mins, 50 mins
class GoalTiming(models.Model):
    goal_timing_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    goalTimings = models.IntegerField(default=0)

    def __str__(self):
        return str(self.goalTimings)


# list of benefits with description
class Benefit(models.Model):
    ben_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    benefitName = models.CharField(max_length=255)
    description = models.CharField(max_length=5000)

    def __str__(self):
        return self.benefitName


# class UserBenefits(models.Model):
#     benefit_id = models.ForeignKey(Benefits, on_delete=models.CASCADE)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.benefitName

# Edit account1 in figma
# weekly - 120 mins (or) custom - user default location
class UserGoal(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.SET(get_sentinel_user))
    goal_frequency_id = models.ForeignKey(
        GoalFrequency, on_delete=models.CASCADE)
    goal_timings_id = models.ForeignKey(GoalTiming, on_delete=models.CASCADE)
    custom_goal_timings = models.IntegerField()
    location = models.CharField(max_length=8000)

    def __str__(self):
        return self.benefitName
