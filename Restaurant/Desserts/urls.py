from django.urls import path
from Desserts.views import *
app_name = 'Desserts'

urlpatterns = [
    path('gulabjamun/',gulabjamun,name='gulabjamun'),
    path('Brownie/',Brownie,name='Brownie'),
]
    