from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.cars.models import CarModel
from apps.cars.serializers import CarModelCreateSerializer, CarModelListSerializer

class CarModelListCreateAPIView(APIView):
    def post(self, request):
        serializer = CarModelCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def get(self, request):
        serializer = CarModelListSerializer(CarModel.objects.all(), many=True)
        return Response(serializer.data)
    

class CarModelRetrieveUpdateDeleteAPIView(APIView):
    def get(self, request, pk):
        serializer = CarModelListSerializer(get_object_or_404(CarModel, pk=pk))
        return Response(serializer.data, status=200)

    def patch(self, request, pk):
        price = get_object_or_404(CarModel, pk=pk)
        serializer = CarModelCreateSerializer(instance=price, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

    def delete(self, request, pk):
        obj = get_object_or_404(CarModel, pk=pk)
        obj.delete()
        return Response(status=204)