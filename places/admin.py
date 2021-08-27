from django.contrib import admin
from django.utils.html import format_html

from places.models import Place, Image, Location


admin.site.register(Image)
admin.site.register(Location)


class ImageInline(admin.TabularInline):
    model = Image
    fields = ("image", "image_preview", "serial_number")
    readonly_fields = ["image_preview"]

    def image_preview(self, obj):
        return format_html("<img src=\"{}\" style=\"max-height: 200px\" />".format(obj.image.url))


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

