from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.profiles.models import Profile
from apps.users.models import CustomUser


@receiver(post_save, sender=CustomUser)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    if hasattr(instance, 'profile'):
        instance.profile.save()
