from django.db import models
from apps.profiles.models import Profile

class Suggestion(models.Model):
    TYPE_CHOICES = [
        ('nutritionist', 'Nutritionist Doctor'),
        ('dietitian', 'Dietitian Doctor'),
        ('acupuncturists', 'Acupuncturists Doctor'),
        ('homeopaths', 'Homeopaths Doctor'),
        ('naturopaths', 'Naturopaths Doctor')
    ]
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    is_saved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.type} - {self.text[:20]}"
