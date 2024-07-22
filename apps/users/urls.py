from django.urls import path
from . import views


urlpatterns = [
    path('', views.CustomUserCreateListAPIView.as_view()),
    path('<int:pk>/', views.CustomUserRetrieveUpdateDeleteAPIView.as_view())    
]