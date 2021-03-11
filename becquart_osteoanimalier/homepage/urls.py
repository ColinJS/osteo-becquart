from django.urls import path
from becquart_osteoanimalier.homepage import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
]