from django.urls import path
from . import views


urlpatterns = [
    path('categories/', views.CategoryListCreateAPIView.as_view()),
    path('category/<int:pk>/', views.CategoryRetrieveUpdateDeleteAPIView.as_view()),

    path('car_washes/', views.CarWashListAPIView.as_view()),
    path('car_wash/<int:pk>/', views.CarWashRetrieveUpdateDeleteAPIView.as_view()),
]