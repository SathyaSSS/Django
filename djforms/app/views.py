from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse


def insert_school(request):
    SCFEO = SchoolForm()
    d = {'SCFEO':SCFEO}

    if request.method == 'POST':
        SCFDO = SchoolForm(request.POST)
        if SCFDO.is_valid():
            scname = SCFDO.cleaned_data['scname']
            scloc = SCFDO.cleaned_data['scloc']
            scprincipal = SCFDO.cleaned_data['scprincipal']

            SCO = School.objects.get_or_create(scname = scname,scloc = scloc,scprincipal = scprincipal)
            return HttpResponse('School is created')

    return render(request,'insert_school.html',d)


def insert_student(request):
    STFEO = StudentForm()
    d={'STFEO':STFEO}

    if request.method == 'POST':
        STFDO = StudentForm(request.POST)
        if STFDO.is_valid():
            scn = STFDO.cleaned_data['scname']
            SO = School.objects.get(scname = scn.scname)
            stn = STFDO.cleaned_data['stdname']
            sta = STFDO.cleaned_data['stdage']

            STO = Student.objects.get_or_create(scname = SO,stdname = stn,stdage = sta)
            return HttpResponse('student is created')
        
    return render(request,'insert_student.html',d)

def Stdforms(request):
    SFEO = StudentForm()
    d={'SFEO':SFEO}

    if request.method == 'POST':
        SFEOD = StudentForm(request.POST)
        if SFEOD.is_valid():
            return HttpResponse(str(SFEOD.cleaned_data))
        
    return render(request,'Stdforms.html',d)

