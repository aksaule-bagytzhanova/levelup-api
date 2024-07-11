from django.contrib import admin
from . import models


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'weight', 'height', 'date_of_birth',)
    list_filter = ('user', )
