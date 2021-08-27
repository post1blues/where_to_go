from django.contrib import admin
from places.models import Place, Image, Location


admin.site.register(Image)
admin.site.register(Location)


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
