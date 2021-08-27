from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from places.models import Place, Location


def home(request):
    locations = Location.objects.all()
    features = []
    if locations:
        for location in locations:
            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [location.lng, location.lat]
                },
                "properties": {
                    "title": location.title,
                    "placeId": location.id,
                    "detailsUrl": reverse("place", kwargs={"id": location.place.id})
                }
            }
            features.append(feature)
    geo_data = {
      "type": "FeatureCollection",
      "features": features
    }
    return render(request, "index.html", context={"data": geo_data})


def place_view(request, id):
    place = get_object_or_404(Place, id=id)
    context = {
        "title": place.title,
        "imgs": [img.image.url for img in place.imgs.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat
        }
    }
    return JsonResponse(context, json_dumps_params={'indent': 2, 'ensure_ascii': False})