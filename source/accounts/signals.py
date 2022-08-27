import os

from django.db.models.signals import pre_save
from django.dispatch import receiver
from accounts.models import Profile


@receiver(pre_save, sender=Profile)
def my_handler(sender, instance, **kwargs):
    if instance.pk and instance.avatar:
        old_img = sender.objects.get(id=instance.pk).avatar.path
        if os.path.exists(old_img):
            os.remove(old_img)
