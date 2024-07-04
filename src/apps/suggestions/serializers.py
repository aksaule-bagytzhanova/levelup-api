from django.conf import settings
import requests
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

        # Генерация текста через ChatGPT
        # generated_text = self.generate_gatgpt_text(prompt)

        # Генерация текста через Gemini
        generated_text = self.generate_gemini_text(prompt)

        return generated_text

    def generate_gemini_text(self, prompt):
        # Отправляем запрос к Gemini API (вымышленный пример)
        response = requests.post(
            f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={settings.GEMINI_API_KEY}",
            json={
                "contents": [
                    {
                        "parts": [
                            {
                                "text": prompt
                            }
                        ]
                    }
                ]
            },
        )

        if response.status_code == 200:
            generated_text = response.json().get('text', '').strip()
        else:
            generated_text = "Ошибка при генерации текста через Gemini."

        return generated_text

    def generate_gatgpt_text(self, prompt):
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
