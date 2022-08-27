from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.


def get_url_path(instance, filename):
    return f"avatars/{instance.user.pk}/{filename}"


class Profile(models.Model):
    avatar = models.ImageField(upload_to=get_url_path, null=True, blank=True, verbose_name="Аватар",
                               validators=[FileExtensionValidator(['jpg', 'jpeg'], "Файлы только jpg и jpeg")])
    about = models.TextField(verbose_name="О себе", null=True)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE,
                                verbose_name="Пользователь", related_name="profile")

    def __str__(self):
        return f"{self.user}"
