from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from places.models import Place


def home(request):
    places = Place.objects.all()
    features = []
    if places:
        for place in places:
            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.lng, place.lat]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": reverse("place", kwargs={"pk": place.id})
                }
            }
            features.append(feature)
    geo_data = {
      "type": "FeatureCollection",
      "features": features
    }
    return render(request, "index.html", context={"data": geo_data})


def place_view(request, pk):
    place = get_object_or_404(Place, id=pk)
    context = {
        "title": place.title,
        "imgs": [img.image.url for img in place.imgs.all()],
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat
        }
    }
    return JsonResponse(
        context,
        json_dumps_params={
            'indent': 2,
            'ensure_ascii': False
        }
    )