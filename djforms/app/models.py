from django.db import models

# Create your models here

class School(models.Model):
    scname = models.CharField(max_length=100,primary_key=True)
    scloc = models.CharField(max_length=100)
    scprincipal = models.CharField(max_length=100)

    def __str__(self):
        return self.scname

class Student(models.Model):
    scname = models.ForeignKey(School,on_delete=models.CASCADE)
    stdname = models.CharField(max_length=100)
    stdage = models.IntegerField()

    def __str__(self):
        return self.stdname
