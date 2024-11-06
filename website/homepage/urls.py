from django.urls import path
from website.homepage import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
]