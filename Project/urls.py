# urls.py

from django.urls import path
from myapp import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('api/insights/', views.InsightListAPIView.as_view(), name='insights_api'),
]

