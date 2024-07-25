from datetime import date
from django.db import models
from django.conf import settings

class Profile(models.Model):
    class GenderChoices(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'

    class TargetChoices(models.TextChoices):
        LOSE_WEIGHT = 'LW', 'Lose Weight'
        GAIN_WEIGHT = 'GW', 'Gain Weight'
        GAIN_MUSCLE_MASS = 'GMM', 'Gain Muscle Mass'
        ADD_PHYSICAL_ACTIVITIES = 'APA', 'Add Physical Activities'

    class TimeLimitChoices(models.TextChoices):
        ONE_MONTH = 'onemonth', 'In one month'
        TWO_WEEK = 'twoweek', 'In two weeks'
        TWO_MONTH = 'twomonth', 'In two months'
        SIX_MONTH = 'sixmonth', 'In six months'

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices, null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    ideal_weight = models.IntegerField(null=True, blank=True)
    target = models.CharField(max_length=128, choices=TargetChoices.choices, null=True, blank=True)
    allergy = models.TextField(null=True, blank=True)
    blood_test_info = models.TextField(null=True, blank=True)
    injuries = models.TextField(null=True, blank=True)
    time_limit = models.CharField(max_length=128, choices=TimeLimitChoices.choices, null=True, blank=True)

    def __str__(self):
        return str(self.user)
    
    def get_age(self):
        if self.date_of_birth:
            today = date.today()
            return today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
            )
        return None
