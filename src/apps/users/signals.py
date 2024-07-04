from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

@receiver(pre_save, sender=User)
def set_unique_username(sender, instance, **kwargs):
    if not instance.username:
        instance.username = instance.email
        if User.objects.filter(username=instance.username).exists():
            instance.username = instance.email + get_random_string(5)
