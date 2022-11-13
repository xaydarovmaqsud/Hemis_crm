from django.shortcuts import render,HttpResponse
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls.base import reverse_lazy
from .models import *
# Create your views here.
def guruh(request):
    context={
        'talaba':Talaba.objects.all(),
        'guruh':Guruh.objects.all()
    }
    return render(request,'guruh.html',context=context)


def byguruh(request,id):
    context={
        'talaba':Talaba.objects.filter(guruh=id),
        'guruh':Guruh.objects.all(),
        'guruh_nomi':Guruh.objects.get(id=id)

    }
    return render(request,'guruh.html',context=context)


def fanlar(request):
    context={
        'mavzu':Mavzu.objects.all(),
        'fan':Fan.objects.all()
    }
    return render(request,'fanlar.html',context=context)


def byfan(request,id):
    context={
        'mavzu':Mavzu.objects.filter(fan=id),
        'fan':Fan.objects.all(),
        'fan_nomi':Fan.objects.get(id=id)

    }
    return render(request,'fanlar.html',context=context)


class TalabaCreate(CreateView):
    model = Talaba
    template_name = 'new.html'
    fields = ['guruh','name','age']

class TalabaUpdate(UpdateView):
    model = Talaba
    template_name = 'edit.html'
    fields = ['guruh','name','age']

class TalabaDelete(DeleteView):
    model = Talaba
    template_name = 'delete.html'
    success_url = reverse_lazy('guruh')


class GuruhCreate(CreateView):
    model = Guruh
    template_name = 'new.html'
    fields = ['name','descriptions']

class GuruhUpdate(UpdateView):
    model = Guruh
    template_name = 'edit.html'
    fields = ['name','descriptions']

class GuruhDelete(DeleteView):
    model = Guruh
    template_name = 'delete.html'
    success_url = reverse_lazy('guruh')

class MavzuCreate(CreateView):
    model = Mavzu
    template_name = 'new.html'
    fields = ['fan','name','soat']

class MavzuUpdate(UpdateView):
    model = Mavzu
    template_name = 'edit.html'
    fields = ['fan','name','soat']

class MavzuDelete(DeleteView):
    model = Mavzu
    template_name = 'delete.html'
    success_url = reverse_lazy('fan')