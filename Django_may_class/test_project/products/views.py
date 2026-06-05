from django.shortcuts import render
from django.views import View
from django.http import HttpResponse as HR
from users.models import students, Animals
import random

# Create your views here.
def recent(request):
    student = students.objects.select_related('profile').prefetch_related('posts')
    return render(request, 'index.html', {'student': student})

def contact(request):
    name = ["Samuel", "abby", "Isreal", "Peter", "Daniel"]
    context = {
        "name" : random.choice(name)
    }
    return render(request, "Details/contact_us.html", context)

class AboutView(View):
    def get(self, request):
        return render(request, "Details/about_us.html")

def animals(request):
    animals = Animals.objects.all()
    context = {
        "animals" : animals
    }
    return render(request, "details/animal.html", context)

def paid(request):
    return HR("This the paid products")

def homePageOne(request):
    return render(request, "home.html")

def homePageTwo(request):
    return render(request, "home1.html")

def homePageThree(request):
    return render(request, "home2.html")

def homePageFive(request):
    return render(request, "home5.html")

def correction(request):
    return render(request, "correction.html")