from django.db import models
from tinymce import models as tinymce_models


class Place(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    short_description = models.TextField(max_length=500, verbose_name="Краткое описание", blank=True)
    long_description = tinymce_models.HTMLField(verbose_name="Полное описание", blank=True)
    lng = models.FloatField(verbose_name="Долгота")
    lat = models.FloatField(verbose_name="Широта")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-date_created"]
        verbose_name = "Место"
        verbose_name_plural = "Места"


class Image(models.Model):
    image = models.ImageField(upload_to="img", verbose_name="Изображение")
    position = models.IntegerField(default=0, verbose_name="Позиция")
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="imgs", verbose_name="Места")

    def __str__(self):
        return f"{self.position} {self.place.title}"

    class Meta:
        ordering = ['serial_number']
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
