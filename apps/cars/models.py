from django.conf import settings
from django.db import models

from apps.users.models import CustomUser
from apps.cars.validators import validate_car_number


class CarModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)

    def __str__(self):
        return self.name + ' ' + self.parent.name
    

class CarService(models.Model):
    number = models.CharField(max_length=10, unique=True, validators=[validate_car_number])
    model = models.ForeignKey(CarModel, on_delete=models.PROTECT, related_name='cars')
    pricing = models.ForeignKey('pricing.Pricing', on_delete=models.PROTECT)
    washer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.washer) + ' ' + str(self.pricing)