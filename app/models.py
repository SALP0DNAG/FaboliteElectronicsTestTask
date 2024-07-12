from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Стандартная модель пользователя с добавлением двух полей:
    Адреса и Информаци о пользователе
    """
    address = models.TextField(max_length=250, blank=True)
    about_me = models.TextField(max_length=250, blank=True)

    def __str__(self):
        return f'{self.username} | {self.email}'
