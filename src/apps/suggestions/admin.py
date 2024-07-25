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


@admin.register(models.Star)
class StarAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(models.StarFood)
class StarFoodAdmin(admin.ModelAdmin):
    list_display = ('star', 'breakfast', 'lunch', 'dinner')
    search_fields = ('star__name', 'breakfast__title', 'lunch__title', 'dinner__title')
    list_filter = ('star__name',)

@admin.register(models.StarSport)
class StarSportAdmin(admin.ModelAdmin):
    list_display = ('star', 'fitness_body_part_type', 'title')
    search_fields = ('star__name', 'title', 'fitness_body_part_type')
    list_filter = ('star__name', 'fitness_body_part_type')

@admin.register(models.ProfileSport)
class ProfileSportAdmin(admin.ModelAdmin):
    list_display = ('profile', 'fitness_body_part_type', 'title')
    search_fields = ('title', 'fitness_body_part_type')
    list_filter = ('profile', 'fitness_body_part_type')
