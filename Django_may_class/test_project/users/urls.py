from django.urls import path
from . import views

urlpatterns = [
    path('', views.user, name='users'),
    path('login/', views.signup, name='login'),
    path('api/user/cart/', views.cart, name='cart')
]