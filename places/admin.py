from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin

from places.models import Place, Image


admin.site.register(Image)


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    fields = ("image", "image_preview", "serial_number")
    readonly_fields = ["image_preview"]
    extra = 1

    def image_preview(self, obj):
        return format_html("<img src=\"{}\" style=\"max-height: 200px\" />".format(obj.image.url))


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

