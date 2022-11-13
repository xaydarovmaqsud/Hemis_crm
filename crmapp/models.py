from django.db import models
from django.urls import reverse
# Create your models here.

class Guruh(models.Model):
    name = models.CharField(max_length=30)
    descriptions = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('guruh')



class Talaba(models.Model):
    guruh = models.ForeignKey(Guruh,related_name='talabalar', on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('guruh')

class Fan(models.Model):
    name = models.CharField(max_length=30)
    descriptions = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Mavzu(models.Model):
    fan = models.ForeignKey(Fan,related_name='fanlar', on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    soat = models.CharField(max_length=10)

    def __str__(self):
        return self.name
