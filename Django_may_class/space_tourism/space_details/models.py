from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    distance = models.CharField(max_length=20)
    travel_time = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class DestinationImage(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='images')
    png = models.ImageField(upload_to='destination_images/png/')
    webp = models.ImageField(upload_to='destination_images/webp/')

    def __str__(self):
        return f"{self.destination} images"
    
class Crew(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return self.name
    
class CrewImage(models.Model):
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE, related_name='images')
    png = models.ImageField(upload_to='crew_images/png/')
    webp = models.ImageField(upload_to='crew_images/webp/')

    def __str__(self):
        return f"{self.crew} images"
    
class Technology(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class TechnologyImage(models.Model):
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE, related_name='images')
    portrait = models.ImageField(upload_to='technology_images/portrait/')
    landscape = models.ImageField(upload_to='technology_images/landscape/')

    def __str__(self):
        return f"{self.technology} images"
    