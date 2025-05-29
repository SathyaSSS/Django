from django import forms
from app.models import *

class SchoolForm(forms.Form):
    scname = forms.CharField(max_length=100)
    scloc = forms.CharField(max_length=100)
    scprincipal = forms.CharField(max_length=100)

class StudentForm(forms.Form):
    scname = forms.ModelChoiceField(queryset=School.objects.all())
    stdname = forms.CharField(max_length=100)
    stdage = forms.IntegerField()
    # Address = forms.CharField(widget=forms.Textarea(attrs={'cols':15,'rows':5}))
    # Email = forms.EmailField()
    # Password = forms.CharField(widget=forms.PasswordInput)
    # Gender = forms.ChoiceField(choices=[('MALE','Male'),('FEMALE','Female')])
    # AdmDate = forms.DateField()

