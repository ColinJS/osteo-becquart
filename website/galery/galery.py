from django.template.loader import render_to_string
from .models import Picture


class Galery:

    def __init__(self, request):
        self.request = request

    def as_slideshow(self):
        pictures = Picture.objects.filter(state=True)
        number_of_pictures = len(pictures)
        return render_to_string("slideshow.html", {"pictures": pictures, "number_of_pictures": number_of_pictures}, self.request)


