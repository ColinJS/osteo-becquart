from django.urls import path
from website.galery import views

urlpatterns = [
    path('slideshow/', views.slideshow, name='slideshow'),
]