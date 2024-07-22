from django.urls import path
from . import views


urlpatterns = [
    path('', views.PricingListCreateAPIView.as_view()),
    path('<int:pk>/', views.PricingRetrieveUpdateDeleteAPIView.as_view())
]