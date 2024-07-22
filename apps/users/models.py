from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


class CustomUser(AbstractUser):
    class Role(models.IntegerChoices):
        DEV = 1
        DIRECTOR = 2
        WASHER = 3

    role = models.IntegerField(choices=Role.choices, default=Role.DEV.value)
    car_wash = models.ForeignKey('washing.CarWash', on_delete=models.CASCADE, null=True, blank=True)

    def clean(self):
        if self.role == self.Role.WASHER.value and not self.car_wash:
            raise ValidationError({'car_wash': 'This field is required'})