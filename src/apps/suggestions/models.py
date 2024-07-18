from django.db import models
from apps.profiles.models import Profile

class Suggestion(models.Model):
    TYPE_CHOICES = [
        ('nutritionist', 'Nutritionist Doctor'),
        ('dietitian', 'Dietitian Doctor'),
        ('fitness', 'Fitness Instructor'),
    ]
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    is_saved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.type} - {self.text[:20]}"


class Food(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    recipe = models.TextField()

    def __str__(self):
        return self.title


class Recommendation(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    breakfast = models.OneToOneField(Food, on_delete=models.CASCADE, related_name='breakfast_recommendations')
    lunch = models.OneToOneField(Food, on_delete=models.CASCADE, related_name='lunch_recommendations')
    dinner = models.OneToOneField(Food, on_delete=models.CASCADE, related_name='dinner_recommendations')

    def __str__(self):
        return f"Recommendation for {str(self.profile)}"


class Star(models.Model):
    name = models.CharField(max_length=200, unique=True)
    avatar = models.ImageField(upload_to='stars/')
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class StarFood(models.Model):
    star = models.ForeignKey(Star, on_delete=models.CASCADE)
    breakfast = models.OneToOneField(Food, on_delete=models.CASCADE, related_name='breakfast_stars')
    lunch = models.OneToOneField(Food, on_delete=models.CASCADE, related_name='lunch_stars')
    dinner = models.OneToOneField(Food, on_delete=models.CASCADE, related_name='dinner_stars')

    def __str__(self) -> str:
        return f"{self.star.name} - {self.breakfast.title}"


class StarSport(models.Model):
    class FitnessBodyPartChoices(models.TextChoices):
        HAND = 'hand', 'Hand'
        LEG = 'leg', 'Leg'
        BACK = 'back', 'Back'
        CHEST = 'chest', 'Chest'
        ASS = 'ass', 'Ass'

    star = models.ForeignKey(Star, on_delete=models.CASCADE)
    fitness_body_part_type = models.CharField(max_length=52, choices=FitnessBodyPartChoices.choices)
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='sports/')
    description = models.TextField()
    video_url = models.URLField()

    def __str__(self) -> str:
        return f"{self.star.name} - {self.fitness_body_part_type} - {self.title}"
