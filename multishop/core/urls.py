from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('accounts/shop/', views.shop, name='shop')
]
