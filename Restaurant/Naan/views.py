from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def plainnaan(request):
    return HttpResponse('<h1> plain Naan with pepper chicken gravy </h1>')

def Butternaan(request):
    return render(request,'Butternaan.html')