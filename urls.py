from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_response/', views.get_response, name='get_response'),
    path('hiragana/', views.hiragana, name='hiragana'),
    path('js/', views.index_js, name='index_js'),
    path('get_response_js/', views.get_response_js, name='js'),
]
