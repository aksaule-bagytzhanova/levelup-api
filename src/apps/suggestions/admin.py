from django.contrib import admin
from . import models


@admin.register(models.Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'type', 'text', 'is_saved')
    list_filter = ('profile', 'type', 'is_saved')
    search_fields = ('profile__user__username', )


@admin.register(models.Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', )
    search_fields = ('title', )


@admin.register(models.Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'profile', )
    list_filter = ('profile', )
