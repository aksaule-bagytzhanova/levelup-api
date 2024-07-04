from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import action

from apps.profiles.models import Profile
from apps.profiles.serializers import ProfileSerializer, ProfileUpdateSerializer

class ProfileViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        try:
            return self.request.user.profile
        except Profile.DoesNotExist:
            raise PermissionDenied("Profile does not exist for this user")

    def retrieve(self, request, pk=None):
        profile = self.get_object()
        serializer = ProfileSerializer(profile)

        return Response(serializer.data)

    def update(self, request, pk=None):
        profile = self.get_object()
        serializer = ProfileUpdateSerializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        profile = serializer.save()
        return Response(ProfileSerializer(profile).data)

    @action(detail=False, methods=['get'])
    def genders(self, request):
        gender_choices = Profile.GenderChoices.choices
        return Response(gender_choices)

    @action(detail=False, methods=['get'])
    def targets(self, request):
        target_choices = Profile.TargetChoices.choices
        return Response(target_choices)
    