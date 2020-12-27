from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import CreateNewUser, CheckUser

# Create your views here.

def login(request):
    if(request.method=='POST'):
        form = CheckUser(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            user =auth.authenticate(username=username,password=password)
            if(user is not None):
                auth.login(request,user)
                nxt = request.GET.get("next", None)
                if nxt is None:
                    messages.info(request,'Login successful')
                    return redirect("/")
                else:
                    if not user.is_superuser:
                        messages.info(request,'Your account doesnt have acces to this page')
                    return redirect(nxt)
            else:
                messages.info(request,'Invalid username or password')
                return render(request,'login.html',{"form":form})

    else:
        nxt = request.GET.get("next", None)
        if nxt is not None:
            messages.info(request,'Please login to see this page.')
        form = CheckUser()
        return render(request,'login.html',{"form":form})


def register(request):

    if(request.method=='POST'):

        form = CreateNewUser(request.POST)

        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            username=form.cleaned_data['username']
            password1=form.cleaned_data['password1']
            password2=form.cleaned_data['password2']
            email=form.cleaned_data['email']

            if(password1==password2):
                if(User.objects.filter(username=username).exists()):
                    messages.info(request,'Username taken')
                    return render(request,'register.html',{"form":form})
                elif(User.objects.filter(email=email).exists()):
                    messages.info(request,'email taken')
                    return render(request,'register.html',{"form":form})
                else:    
                    user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                    user.save()
                    print('user created')
                    messages.info(request,'Register successful')
                    return redirect('login')
            else:
                messages.info(request,'password not matching...')
                return render(request,'register.html',{"form":form})
            
            return redirect('/')

        else:
            messages.info(request,'Forma nije validna!')
            return render(request,'register.html')
    else:
        form = CreateNewUser()
        return render(request,'register.html',{"form":form})


def logout(request):
    auth.logout(request)
    messages.info(request,'Logout successful')
    return redirect('/')