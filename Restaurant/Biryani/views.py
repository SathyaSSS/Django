from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def chickenbiryani(request):
    return HttpResponse('<h1>Namma Ooru Chicken Biryani</h1>')

def Beefbiryani(request):
    return render(request,'Beefbiryani.html')