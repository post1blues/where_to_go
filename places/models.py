from django.db import models
from tinymce import models as tinymce_models


class Place(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description_short = models.TextField(max_length=500, verbose_name="Краткое описание")
    description_long = tinymce_models.HTMLField(null=True, blank=True, verbose_name="Полное описание")
    lng = models.FloatField(verbose_name="Долгота")
    lat = models.FloatField(verbose_name="Широта")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_date"]
        verbose_name = "Место"
        verbose_name_plural = "Места"


class Location(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    lng = models.FloatField(verbose_name="Долгота")
    lat = models.FloatField(verbose_name="Широта")
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name="Места")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.lng}, {self.lat}"

    class Meta:
        ordering = ["-created_date"]
        verbose_name = "Локация"
        verbose_name_plural = "Локации"


class Image(models.Model):
    image = models.ImageField(upload_to="img", verbose_name="Изображение")
    serial_number = models.IntegerField(default=0, verbose_name="Позиция")
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="imgs", verbose_name="Места")

    def __str__(self):
        return f"{self.serial_number} {self.place.title}"

    class Meta:
        ordering = ['serial_number']
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
