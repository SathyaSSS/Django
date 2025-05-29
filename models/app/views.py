from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from app.models import *


def insert_Topic(request):
    tn = input('Enter topic name :')
    TTO = Topic.objects.get_or_create(topic_name = tn)
    if TTO[1]:
        return HttpResponse(f'{tn} is created')
    else:
        return HttpResponse(f'{tn} is already created')
    
    
def insert_webpage(request):
    tn = input('Enter topic name :')
    LTO = Topic.objects.filter(topic_name = tn)
    if LTO:
        name = input('Enter the name :')
        url = input('Enter the url :')
        email = input('Enter the email :')
        age = input('Enter the age :')
        TO = LTO[0]
        TWO = webpage.objects.get_or_create(topic_name = TO,name = name,url = url,email = email,age = age)
        if TWO[0]:
            return HttpResponse(f'{name} is created')
        else:
             return HttpResponse(f'{name} is already created')
    else:
        return HttpResponse(f'{tn} parent Topic is not available')
            

def insert_AccessRecord(request):
    name = input('Enter primary key of webpage :')
    WO = webpage.objects.get(name = name)
    date = input('Enter the Date')
    author = input('Enter author Name :')
    TAO = AccessRecord.objects.get_or_create(name = WO,date = date,author = author)
    if TAO[0]:
        return HttpResponse(f'{name} is created')
    else:
        return HttpResponse(f'{name} is Already exist')


def display_Topic(request):
    TO = Topic.objects.all()
    d={'TO':TO}
    return render(request,'display_Topic.html',d)

def display_webpage(request):
    WO = webpage.objects.all()
    d1={'WO':WO}
    return render(request,'display_webpage.html',d1)

def display_AccessRecord(request):
    ARO = AccessRecord.objects.all()
    d2 = {'ARO':ARO}
    return render(request,'display_AccessRecord.html',d2)

def update_Topic(request):
    Topic.objects.filter(topic_name='swimming').update(topic_name ='swim')
    UTO = Topic.objects.all()
    d3 = {'UTO':UTO}
    return render(request,'update_Topic.html',d3)

def update_webpage(request):
    TO = Topic.objects.all()
    webpage.objects.filter(name ='sathya1').update(topic_name =TO)
    UWO = webpage.objects.all()
    d3 = {'UWO':UWO}
    return render(request,'update_webpage.html',d3)