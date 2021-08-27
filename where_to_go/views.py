from django.shortcuts import render
from places.models import Place, Image


def home(request):
    places = Place.objects.all()
    features = []
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
                "detailsUrl": place.details.url
            }
        }
        features.append(feature)

    data = {
      "type": "FeatureCollection",
      "features": features
    }
    print(data)
    return render(request, "index.html", context={"data": data})
