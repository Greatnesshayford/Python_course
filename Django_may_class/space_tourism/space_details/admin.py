from django.contrib import admin
from .models import Destination, DestinationImage, Crew, CrewImage, Technology, TechnologyImage

# Register your models here.
@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'distance', 'travel_time')
    search_fields = ('name',)

@admin.register(DestinationImage)
class DestinationImageAdmin(admin.ModelAdmin):
    list_display = ('destination',)
    search_fields = ('destination__name',)
    list_filter = ('png', 'webp')

@admin.register(Crew)
class CrewAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')
    search_fields = ('name', 'role')

@admin.register(CrewImage)
class CrewImageAdmin(admin.ModelAdmin):
    list_display = ('crew',)
    search_fields = ('crew__name',)
    list_filter = ('png', 'webp')

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(TechnologyImage)
class TechnologyImageAdmin(admin.ModelAdmin):
    list_display = ('technology',)
    search_fields = ('technology__name',)
    list_filter = ('portrait', 'landscape')
