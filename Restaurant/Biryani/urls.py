from django.urls import path
from Biryani.views import *
app_name = 'Biryani'

urlpatterns =[
    path('chickenbiryani/',chickenbiryani,name='chickenbiryani'),
    path('Beefbiryani/',Beefbiryani,name='Beefbiryani'),
]