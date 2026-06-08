from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import get_crew_json, get_destination_json, get_technology_json, crew, destination, technology, home

urlpatterns = [
    path('/api/crew/', get_crew_json, name='get_crew_json'),
    path('/api/destination/', get_destination_json, name='get_destination_json'),
    path('/api/technology/', get_technology_json, name='get_technology_json'),
    path('crew/', crew, name='crew'),
    path('destination/', destination, name='destination'),
    path('technology/', technology, name='technology'),
    path('', home, name='home')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
