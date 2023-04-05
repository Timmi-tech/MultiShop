from django.urls import path
from . import views

urlpatterns = [
    path('accounts/login/', views.signin, name='login'),
    path('accounts/register/', views.register, name='register'),
    path('activate/<email_token>/', views.activate, name='activate'),
    path('accounts/logout/', views.logout, name='logout'),
    path('accounts/cart/', views.cart, name='cart'),
    path('accounts/checkout/', views.checkout, name='checkout'),
    path('add_to_cart/<slug>/', views.add, name='add_to_cart'),
    path('remove_from_cart/<slug>/', views.remove, name='remove_from_cart'),
    path('remove_from_cart_item/<slug>/', views.remove_item, name='remove_from_cart_item'),
]
