from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def gulabjamun(request):
    return HttpResponse('<h1> Gulabjamun with ice cream....</h1>')

def Brownie(request):
    return render(request,'Brownie.html')