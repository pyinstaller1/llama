# japan_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # 기본 경로
    path('get_response/', views.get_response, name='get_response'),  # 분석 경로
]
