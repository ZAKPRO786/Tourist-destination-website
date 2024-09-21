from django.db import models

# Create your models here.
class TouristDestination(models.Model):
    place_name = models.CharField(max_length=100)
    weather = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    google_map_link = models.URLField(max_length=200)
    image = models.ImageField(upload_to='destination_images/')
    description = models.TextField()

    def __str__(self):
        return self.place_name