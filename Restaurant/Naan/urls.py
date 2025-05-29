from django.urls import path
from Naan.views import *
app_name = 'Naan'

urlpatterns =[
    path('plainnaan/',plainnaan,name='plainnaan'),
    path('Butternaan/',Butternaan,name='Butternaan'),
]   