import os
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from .models import Food
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .forms import AddNewFood

# Create your views here.

def index(request):

    foods=Food.objects.all()
    return render(request,"index.html",{'foods' : foods})



def search(request):
    
    foods=Food.objects.all()
    
    newFoods=[]
    search=request.GET["search"]
    if(search!=""): 
        for food in foods:
            if(food.name==search):
                newFoods.append(food)
            elif(str(food.price)==search):
                newFoods.append(food)
        foods=newFoods 

    return render(request,"index.html",{'foods' : foods})


def detail(request, detail):

    if(Food.objects.filter(id=detail).exists()):
        food=Food.objects.get(id=detail)
        
    return render(request,"detail.html",{'food':food})


def add(request):        
    if(request.method=='POST'):

        form = AddNewFood(request.POST,request.FILES)
        
        '''name=request.POST['name']
        img=request.FILES['img']
        desc=request.POST['desc']
        price=request.POST['price']'''
        if form.is_valid():
            name=form.cleaned_data['name']
            img=form.cleaned_data['img']
            desc=form.cleaned_data['desc']
            price=form.cleaned_data['price']

            try:
                pass
                tmp = int(price)
            except ValueError:
                messages.info(request,'Mora Broj!')
                return render(request,"add.html",{'form':form})
            else:
                price=tmp
                #fs=FileSystemStorage()
                #fs.save(img.name,img)

                newFood=Food(name=name,img=img,desc=desc,price=price)
                newFood.save()

            return redirect('/')
        else:
            #nije validna forma
            messages.info(request,'nije validna forma')
            return render(request,"add.html",{'form':form})
    else:
        form = AddNewFood()
        return render(request,"add.html",{'form':form})


def delete(request, id):
    if(Food.objects.filter(id=id).exists()):
        food=Food.objects.get(id=id)

        fs=FileSystemStorage()
        fs.delete(food.img.name)
        food.delete()

    return redirect('/')

