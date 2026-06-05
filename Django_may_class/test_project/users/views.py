from django.shortcuts import render
from django.http import HttpResponse
from .models import students

# Create your views here.
def user(request):
    return HttpResponse("welcome user")
def signup(request):
    return HttpResponse("sign in to your account.")
def cart(request):
    return HttpResponse("This is your cart")