from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='blockchain-home'),
    path('add_product/', views.add_product,name='blockchain-add-product'),
    path('about/', views.about,name='blockchain-about'),
    path('tracking/', views.tracking, name='product-tracking'),
    path('enter/',views.enter_prod_id, name="blockchain-your-product"),
]