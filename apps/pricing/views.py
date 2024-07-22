from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.pricing.models import Pricing
from apps.pricing.serializers import PricingListSerializer


class PricingListCreateAPIView(APIView):
    def post(self, request):
        serializer = PricingListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def get(self, request):
        serializer = PricingListSerializer(Pricing.objects.all(), many=True)
        return Response(serializer.data)
    

class PricingRetrieveUpdateDeleteAPIView(APIView):
    def get(self, request, pk):
        serializer = PricingListSerializer(get_object_or_404(Pricing, pk=pk))
        return Response(serializer.data, status=200)

    def delete(self, request, pk):
        obj = get_object_or_404(Pricing, pk=pk)
        obj.delete()
        return Response(status=204)