from django.shortcuts import render
from django.views import View
from django.http import HttpResponse as HR
from users.models import students, Animals
import random
from .forms import ContactForm

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
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f"Alert!!!, {name} with email {email} just sent the message {message}")

    return render(request, "home.html")

def homePageTwo(request):
    form = ContactForm()
    context = {
        "form" : form
    }
    return render(request, "home1.html", context)

def homePageThree(request):
    return render(request, "home2.html")

def homePageFive(request):
    return render(request, "home5.html")

def correction(request):
    return render(request, "correction.html")