from django.contrib import admin
from .models import JournalHistoryDetail

# Register your models here.


@admin.register(JournalHistoryDetail)
class JournalHistoryDetailModel(admin.ModelAdmin):
    list_filter = ('user_id', 'location', 'noOfMinutes',
                   'startDateTime', 'createdDateTime')
    list_display = ('user_id', 'location', 'noOfMinutes',
                    'startDateTime', 'createdDateTime')
