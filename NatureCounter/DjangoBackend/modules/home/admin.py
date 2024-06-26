from django.contrib import admin
from .models import Benefit, GoalTiming, GoalFrequency

# Register your models here.


@admin.register(GoalFrequency)
class GoalFrequencyModel(admin.ModelAdmin):
    list_filter = ('goalFrequency',)
    list_display = ('goalFrequency',)


admin.site.register(GoalTiming)

# @admin.register(GoalTiming)
# class GoalTimingModel(admin.ModelAdmin):
#     list_filter = ('goalTimings',)
#     list_display = ('goalTimings',)


@admin.register(Benefit)
class BenefitModel(admin.ModelAdmin):
    list_filter = ('benefitName', 'description')
    list_display = ('benefitName', 'description')
