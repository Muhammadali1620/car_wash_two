from django.urls import path
from . import views


urlpatterns = [
    path('car_models/', views.CarModelListCreateAPIView.as_view()),
    path('car_model/<int:pk>/', views.CarModelRetrieveUpdateDeleteAPIView.as_view()),
]