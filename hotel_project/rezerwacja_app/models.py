from django.db import models

# Create your models here.

class Pokoj(models.Model):
    nrPokoju = models.IntegerField()
    nazwa = models.CharField(max_length=30)
    liczbaOsob = models.IntegerField()
    dlaNiepelnosprawnych = models.BooleanField()

class Gosc(models.Model):
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=30)
    email = models.EmailField()

class Rezerwacja(models.Model):
    gosc = models.ForeignKey(Gosc, on_delete=models.CASCADE)
    pokoj = models.ForeignKey(Pokoj, on_delete=models.CASCADE)
    dataPrzyjazdu = models.DateField()
    dataWyjazdu = models.DateField()
