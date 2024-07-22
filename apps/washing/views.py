from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.washing.serializers import CarWashListSerializer, CategoryCreateSerializer, CategoryListSerializer 
from apps.washing.models import CarWash, Category


class CategoryListCreateAPIView(APIView):
    def post(self, request):
        serializer = CategoryCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def get(self, request):
        serializer = CategoryListSerializer(Category.objects.all(), many=True)
        return Response(serializer.data)


class CategoryRetrieveUpdateDeleteAPIView(APIView):
    def get(self, request, pk):
        serializer = CategoryListSerializer(get_object_or_404(Category, pk=pk))
        return Response(serializer.data, status=200)
    
    def patch(self, request, pk):
        price = get_object_or_404(Category, pk=pk)
        serializer = CategoryCreateSerializer(instance=price, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

    def delete(self, request, pk):
        obl = get_object_or_404(Category, pk=pk)
        obl.delete()
        return Response(status=204)
    

class CarWashListAPIView(APIView):
    def post(self, request):
        serializer = CarWashListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def get(self, request):
        serializer = CarWashListSerializer(CarWash.objects.all(), many=True)
        return Response(serializer.data)
    

class CarWashRetrieveUpdateDeleteAPIView(APIView):
    def get(self, request, pk):
        serializer = CarWashListSerializer(get_object_or_404(CarWash, pk=pk))
        return Response(serializer.data, status=200)

    def patch(self, request, pk):
        price = get_object_or_404(CarWash, pk=pk)
        serializer = CarWashListSerializer(instance=price, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

    def delete(self, request, pk):
        obj = get_object_or_404(CarWash, pk=pk)
        obj.delete()
        return Response(status=204)