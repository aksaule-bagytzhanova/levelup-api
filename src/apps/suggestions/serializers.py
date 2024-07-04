from django.utils import timezone
from rest_framework import serializers

from .models import Suggestion

class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = '__all__'

class SuggestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = ['type']

    def create(self, validated_data):
        profile = self.context['request'].user.profile
        text = self.generate_text()
        suggestion = Suggestion.objects.create(profile=profile, text=text, is_saved=False, **validated_data)
        return suggestion

    def generate_text(self):
        # Ваша логика генерации текста
        return f"Suggestion created at {timezone.now()}"

class SuggestionSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = ['is_saved']
