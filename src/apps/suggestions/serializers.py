import json
from django.conf import settings
from django.db import transaction
import requests
from rest_framework import serializers
from openai import OpenAI

from .models import ProfileSport, Star, StarFood, StarSport, Suggestion, Recommendation, Food
from apps.suggestions.prompt import ChatGPTProfileSportRequestTemplate, ChatGPTRequestTemplate, ChatGPTRecommendationRequestTemplate

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

        generated_text = ""
        if response.status_code == 200:
            candidates = response.json().get('candidates', [])
            if len(candidates) == 0:
                return generated_text
            
            content = candidates[0].get('content', {})
            if 'parts' not in content:
                return generated_text
            
            parts = content.get('parts', [])
            if len(parts) == 0:
                return generated_text
            
            part = parts[0]
            if 'text' not in part:
                return generated_text
            
            generated_text = part.get('text')
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


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


class RecommendationSerializer(serializers.ModelSerializer):
    breakfast = FoodSerializer(read_only=True)
    lunch = FoodSerializer(read_only=True)
    dinner = FoodSerializer(read_only=True)

    class Meta:
        model = Recommendation
        fields = ['id', 'profile', 'created_at', 'breakfast', 'lunch', 'dinner']


class RecommendationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = []

    def create(self, validated_data):
        profile = self.context['request'].user.profile
        data = self.generate_data(profile)
        
        # Создаем объекты Food для каждого приема пищи
        breakfast = Food.objects.create(
            title=data['breakfast']['title'],
            description=data['breakfast']['description'],
            recipe=data['breakfast']['recipe']
        )

        lunch = Food.objects.create(
            title=data['lunch']['title'],
            description=data['lunch']['description'],
            recipe=data['lunch']['recipe']
        )

        dinner = Food.objects.create(
            title=data['dinner']['title'],
            description=data['dinner']['description'],
            recipe=data['dinner']['recipe']
        )

        # Создаем объект Recommendation, связывая его с профилем и блюдами
        recommendation = Recommendation.objects.create(
            profile=profile,
            breakfast=breakfast,
            lunch=lunch,
            dinner=dinner
        )
        return recommendation

    def generate_data(self, profile):
        # Формируем запрос на основе типа рекомендации
        prompt = ChatGPTRecommendationRequestTemplate.generate_request(profile)

        # Генерация текста через ChatGPT
        generated_text = self.generate_gatgpt_text(prompt)
        print(generated_text)
        generated_text = generated_text.replace("'", '"')

        data = json.loads(generated_text)

        return data

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


class StarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Star
        fields = '__all__'

class StarFoodSerializer(serializers.ModelSerializer):
    breakfast = FoodSerializer(read_only=True)
    lunch = FoodSerializer(read_only=True)
    dinner = FoodSerializer(read_only=True)

    class Meta:
        model = StarFood
        fields = '__all__'

class StarSportSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    class Meta:
        model = StarSport
        fields = '__all__'

    def get_photo(self, obj):
        request = self.context.get('request')
        if obj.photo and request:
            return request.build_absolute_uri(obj.photo.url)
        return None


class ProfileSportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileSport
        fields = '__all__'


class ProfileSportCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileSport
        fields = []

    def create(self, validated_data):
        profile = self.context['request'].user.profile
        data = self.generate_data(profile)
        
        created_instances = []
        with transaction.atomic():
            for part, exercises in data.items():
                for exercise in exercises:
                    profile_sport = ProfileSport(
                        profile=profile,
                        fitness_body_part_type=part,
                        title=exercise['title'],
                        description=exercise['description'],
                        photo=None,
                        video_url=None
                    )
                    profile_sport.save()
                    created_instances.append(profile_sport)
        
        return created_instances
    

    def generate_data(self, profile):
        # Формируем запрос на основе типа рекомендации
        prompt = ChatGPTProfileSportRequestTemplate.generate_request(profile)

        # Генерация текста через ChatGPT
        generated_text = self.generate_gatgpt_text(prompt)
        generated_text = generated_text.replace("'", '"')

        data = json.loads(generated_text)

        return data

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

class ProfileSportSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileSport
        fields = ['is_saved']
