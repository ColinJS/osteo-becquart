from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from becquart_osteoanimalier.galery.galery import Galery
from django.core.cache import cache


def home_page(request):

    if request.method == 'GET':
        valid = {"status": False, "message": ""}
    else:
        form = ContactForm(request.POST)
        valid = {"status": True, "message": "Message envoyé avec succès"}
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['becquart.osteo@gmail.com'])
            except BadHeaderError:
                valid = {"status": False, "message": "Erreur d'envois, veuillez réessayer"}

    form = ContactForm()
    galery = Galery(request)

    return render(request, "homepage.html", {"form": form, "valid": valid, "galery": galery.as_slideshow()})
