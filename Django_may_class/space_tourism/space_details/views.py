from django.shortcuts import render
from django.http import JsonResponse
from .models import Crew, Destination, Technology

# Create your views here.
def get_crew_json(request):
    crew_data = Crew.objects.prefetch_related('images') #.values("name", "role", "bio", "images__png", "images__webp").all()
    data = []
    for crew in crew_data:
        data.append({
            "name": crew.name,
            "role": crew.role,
            "bio": crew.bio,
            "images": {
                "png": crew.images.all()[0].png.url, #crew["images__png"].url,
                "webp": crew.images.all()[0].webp.url
            }
        })
    return JsonResponse(data, safe=False)

def get_destination_json(request):
    destination_data = Destination.objects.prefetch_related('images')
    data = []
    for destination in destination_data:
        data.append({
            "name": destination.name,
            "description": destination.description,
            "distance": destination.distance,
            "travel": destination.travel_time,
            "images": {
                "png": destination.images.all()[0].png.url,
                "webp": destination.images.all()[0].webp.url
            }
        })
    return JsonResponse(data, safe=False)

def get_technology_json(request):
    technology_data = Technology.objects.prefetch_related('images')
    data = []
    for technology in technology_data:
        data.append({
            "name": technology.name,
            "description": technology.description,
            "images": {
                "portrait": technology.images.all()[0].portrait.url,
                "landscape": technology.images.all()[0].landscape.url
            }
        })
    return JsonResponse(data, safe=False)

def home(request):
    return render(request, 'index.html')

def crew(request):
    # crew_data = Crew.objects.prefetch_related('images')
    # context = {
    #     "crew": crew_data
    # }
    return render(request, 'crews.html')

def destination(request):
    destination_data = Destination.objects.filter(name = "Moon").prefetch_related('images')
    data = {}
    for destination in destination_data:
        data = {
            "name": destination.name,
            "description": destination.description,
            "distance": destination.distance,
            "travel_time": destination.travel_time,
            "images": {
                "png": destination.images.all()[0].png.url,
                "webp": destination.images.all()[0].webp.url
            }
        }
    context = {
        "destination": data
    }
    return render(request, 'destination.html', context)

def technology(request):
    technology_data = Technology.objects.filter(name = "Launch vehicle").prefetch_related('images')
    data = {}
    for technology in technology_data:
        data = {
            "name": technology.name,
            "description": technology.description,
            "images": {
                "portrait": technology.images.all()[0].portrait.url,
                "landscape": technology.images.all()[0].landscape.url
            }
        }
    context = {
        "technology": data
    }
    return render(request, 'technology.html', context)