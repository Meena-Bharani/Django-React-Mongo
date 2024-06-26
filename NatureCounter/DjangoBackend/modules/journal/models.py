# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models

# Create your models here.


class JournalHistoryDetail(models.Model):
    # user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=2000)
    noOfMinutes = models.IntegerField(default=0)
    startDateTime = models.DateTimeField(auto_now=False, auto_now_add=False)
    createdDateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
