from django.utils import timezone
from rest_framework import status
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Star, StarFood, StarSport, Suggestion, Recommendation, ProfileSport
from .serializers import ProfileSportCreateSerializer, ProfileSportSaveSerializer, ProfileSportSerializer, StarFoodSerializer, StarSerializer, StarSportSerializer, SuggestionSerializer, SuggestionCreateSerializer, SuggestionSaveSerializer, RecommendationSerializer, RecommendationCreateSerializer

class SuggestionViewSet(viewsets.ModelViewSet):
    queryset = Suggestion.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return SuggestionCreateSerializer
        elif self.action == 'save_suggestion':
            return SuggestionSaveSerializer
        return SuggestionSerializer

    def get_queryset(self):
        queryset = Suggestion.objects.filter(profile__user=self.request.user).order_by('-created_at')
        type_filter = self.request.query_params.get('type', None)
        if type_filter:
            queryset = queryset.filter(type=type_filter)
        return queryset
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        suggestion = serializer.save()
        output_serializer = SuggestionSerializer(suggestion)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'])
    def saved(self, request):
        queryset = self.get_queryset().filter(is_saved=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def save_suggestion(self, request, pk=None):
        suggestion = self.get_object()
        serializer = self.get_serializer(suggestion, data={'is_saved': True}, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 'suggestion saved'})

    @action(detail=False, methods=['get'])
    def types(self, request):
        type_choices = Suggestion.TYPE_CHOICES
        return Response(type_choices)


class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return RecommendationCreateSerializer
        return RecommendationSerializer

    def get_queryset(self):
        queryset = Recommendation.objects.filter(profile__user=self.request.user).order_by('-created_at')
        return queryset
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        suggestion = serializer.save()
        output_serializer = RecommendationSerializer(suggestion)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)


class StarViewSet(viewsets.ModelViewSet):
    queryset = Star.objects.all()
    serializer_class = StarSerializer

    @action(detail=True, methods=['get'])
    def foods(self, request, pk=None):
        star = self.get_object()
        foods = StarFood.objects.filter(star=star).select_related('breakfast', 'lunch', 'dinner')
        serializer = StarFoodSerializer(foods, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def sports(self, request, pk=None):
        star = self.get_object()
        sports = StarSport.objects.filter(star=star)
        serializer = StarSportSerializer(sports, many=True, context={'request': request})
        return Response(serializer.data)

class StarFoodViewSet(viewsets.ModelViewSet):
    queryset = StarFood.objects.all()
    serializer_class = StarFoodSerializer

class StarSportViewSet(viewsets.ModelViewSet):
    queryset = StarSport.objects.all()
    serializer_class = StarSportSerializer

class ProfileSportViewSet(viewsets.ModelViewSet):
    queryset = ProfileSport.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return ProfileSportCreateSerializer
        elif self.action == 'save_profile_sport':
            return ProfileSportSaveSerializer
        return ProfileSportSerializer

    def get_queryset(self):
        queryset = ProfileSport.objects.filter(profile__user=self.request.user).order_by('-created_at')

        return queryset

    def list(self, request, *args, **kwargs):
        parts = ["hand", "leg", "back", "chest", "press"]
        result = []
        for part in parts:
            part_queryset = self.get_queryset().filter(fitness_body_part_type=part)[:3]
            result.extend(part_queryset)
        serializer = self.get_serializer(result, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        profile_sport = self.get_object()
        serializer = ProfileSportSerializer(profile_sport)
        return Response(serializer.data)

    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        created_sports = serializer.save()
        output_serializer = ProfileSportSerializer(created_sports, many=True)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'])
    def saved(self, request):
        queryset = self.get_queryset().filter(is_saved=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def save_profile_sport(self, request, pk=None):
        profile_sport = self.get_object()
        serializer = self.get_serializer(profile_sport, data={'is_saved': True}, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 'profile sport saved'})
