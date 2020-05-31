from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='blockchain-home'),
    path('about/', views.about,name='blockchain-about'),
]