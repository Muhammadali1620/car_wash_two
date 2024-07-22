from rest_framework import serializers
from apps.washing.models import Category, CarWash
from django.template.defaultfilters import slugify


class CategoryCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)

    def create(self, validated_data):
        validated_data['slug'] = slugify(validated_data['name'])
        if Category.objects.filter(slug=validated_data['slug']).exists():
            raise serializers.ValidationError('This slug already exists')
        return Category.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.save()
        return instance
    
    def to_internal_value(self, data):
        return super().to_internal_value(data)

    def to_representation(self, instance):
        return super().to_representation(instance)
    
    def validate(self, attrs):
        return super().validate(attrs)
    
    # def validate_slug(self, value):
    #     if Category.objects.filter(slug=value).exists():
    #         raise serializers.ValidationError('This slug already exists')
    #     return value


class CategoryListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    slug = serializers.SlugField(max_length=50)



class CarWashListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarWash
        fields = '__all__'