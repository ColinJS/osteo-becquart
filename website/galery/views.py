from django.shortcuts import render
from .models import Picture


def slideshow(request):

    pictures = Picture.objects.filter(state=True)
    print(pictures)
    number_of_pictures = len(pictures)
    return render(request, "slideshow.html", {"pictures": pictures, "number_of_pictures": number_of_pictures})

