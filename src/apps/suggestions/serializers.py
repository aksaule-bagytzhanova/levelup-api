from django.conf import settings
from rest_framework import serializers
from openai import OpenAI

from .models import Suggestion
from apps.suggestions.prompt import ChatGPTRequestTemplate

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
        text = self.generate_text(profile, validated_data['type'])
        suggestion = Suggestion.objects.create(profile=profile, text=text, is_saved=False, **validated_data)
        return suggestion

    def generate_text(self, profile, suggestion_type):
        # Формируем запрос на основе типа рекомендации
        prompt = ChatGPTRequestTemplate.generate_request(profile, suggestion_type)

        # Отправляем запрос к ChatGPT API
        client = OpenAI(api_key=settings.OPENAI_API_KEY)
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        generated_text = completion.choices[0].message.content
        return generated_text

class SuggestionSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = ['is_saved']
