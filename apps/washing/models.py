from django.db import models
from django.conf import settings

from apps.users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class CarWash(models.Model):
    name = models.CharField(max_length=250)
    director = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                 on_delete=models.CASCADE, 
                                 limit_choices_to={'role': CustomUser.Role.DIRECTOR.value})
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name