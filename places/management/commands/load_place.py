from json import JSONDecodeError

from django.core.management.base import BaseCommand
from django.core.files import File
import requests
from time import sleep
from io import BytesIO

from places.models import Place
from places.models import Image


class Command(BaseCommand):
    help = "Download places and load them into db"

    def add_arguments(self, parser):
        parser.add_argument("url", type=str, help="Request url")
        parser.add_argument("-a", "--attempts", type=int, help="Number of attempts")

    def handle(self, *args, **options):
        attempts = options["attempts"]

        if not attempts:
            attempts = 3

        url = options["url"]

        place_response = self._get(url, attempts)

        try:
            place_data = place_response.json()
        except JSONDecodeError:
            self.stdout.write(self.style.ERROR("Response doesn't contain json"))
            exit()

        place = self._create_place(place_data)

        if "imgs" in place_data:
            for idx, img_url in enumerate(place_data["imgs"]):
                img_response = self._get(img_url, attempts)

                if not img_response:
                    continue

                image = {
                    "img_binary": img_response.content,
                    "img_name": img_url.strip().split("/")[-1],
                    "serial_number": idx + 1,
                    "place": place
                }
                self._create_image(image)

        self.stdout.write(self.style.SUCCESS("New place with photos were created successfully"))

    def _create_place(self, place_data):
        created_place, created = Place.objects.get_or_create(
            title=place_data["title"],
            description_short=place_data["description_short"],
            description_long=place_data["description_long"],
            lng=place_data["coordinates"]["lng"],
            lat=place_data["coordinates"]["lat"]
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"New place \"{place_data['title']}\" added into db"))
        else:
            self.stdout.write(self.style.WARNING(f"Place \"{place_data['title']}\" is already in db"))
            exit()
        return created_place

    def _create_image(self, image):
        image_blob = BytesIO(image["img_binary"])

        image_obj = Image(
            serial_number=image["serial_number"],
            place=image["place"]
        )
        image_obj.image.save(image["img_name"], File(image_blob), save=True)

    def _get(self, url, attempts):
        for i in range(attempts):
            self.stdout.write(self.style.NOTICE(f"Request {url} - attempt {i + 1}/{attempts}"))
            try:
                response = requests.get(url)
                response.raise_for_status()
                return response
            except requests.HTTPError:
                sleep(5)
        self.stdout.write(self.style.ERROR(f"Could't get response in {attempts} attempts from {url}"))
        exit()
