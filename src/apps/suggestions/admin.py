from django.contrib import admin
from . import models


@admin.register(models.Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'type', 'text', 'is_saved')
    list_filter = ('profile', 'type', 'is_saved')
    search_fields = ('profile__user__username', )
