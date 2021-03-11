from django.urls import path
from becquart_osteoanimalier.galery import views

urlpatterns = [
    path('slideshow/', views.slideshow, name='slideshow'),
]