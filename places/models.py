from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=100)
    description_short = models.CharField(max_length=500)
    description_long = models.TextField()
    lng = models.FloatField()
    lat = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Location(models.Model):
    title = models.CharField(max_length=100)
    lng = models.FloatField()
    lat = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.lng}, {self.lat}"


class Image(models.Model):
    image = models.ImageField(upload_to="img")
    serial_number = models.IntegerField()
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="imgs")

    def __str__(self):
        return f"{self.serial_number} {self.place.title}"
