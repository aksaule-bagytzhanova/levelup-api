from django.utils import timezone
from rest_framework import status
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Suggestion
from .serializers import SuggestionSerializer, SuggestionCreateSerializer, SuggestionSaveSerializer

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
