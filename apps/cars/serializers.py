from django.template.defaultfilters import slugify

from rest_framework import serializers

from apps.cars.models import CarModel, CarService


class CarModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'


class CarModelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        exclude = ('slug')

    def create(self, validated_data):
        validated_data['slug'] = slugify(validated_data['name'])
        if CarModel.objects.filter(slug=validated_data['slug']).exists():
            raise serializers.ValidationError('This slug already exists')
        return super().create(validated_data)