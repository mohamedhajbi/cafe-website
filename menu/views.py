from django.shortcuts import render
from . import models

def menu(request):
    categories=models.Categories.objects.all()
    return render(request, 'menu/menu.html',{'categories':categories})

def list(request,id):
    categories=models.Categories.objects.get(id=id)
    list=models.List.objects.filter(categories=categories)
    return render(request, 'menu/list.html',{'categories':categories,'list':list}) 