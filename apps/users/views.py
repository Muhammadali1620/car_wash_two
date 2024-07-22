from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.users.models import CustomUser
from apps.users.serializers import CustomUserCreateSerializer, CustomUserListSerializer, CustomUserUpdateSerializer


class CustomUserCreateListAPIView(APIView):
    def post(self, request):
        serializer = CustomUserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def get(self, request):
        serializer = CustomUserListSerializer(CustomUser.objects.all(), many=True)
        return Response(serializer.data)
    

class CustomUserRetrieveUpdateDeleteAPIView(APIView):
    def get(self, request, pk):
        serializer = CustomUserListSerializer(get_object_or_404(CustomUser, pk=pk))
        return Response(serializer.data, status=200)

    def patch(self, request, pk):
        price = get_object_or_404(CustomUser, pk=pk)
        serializer = CustomUserUpdateSerializer(instance=price, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

    def delete(self, request, pk):
        obj = get_object_or_404(CustomUser, pk=pk)
        obj.delete()
        return Response(status=204)