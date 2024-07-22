from rest_framework import serializers

from apps.pricing.models import Pricing


class PricingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricing
        fields = '__all__'