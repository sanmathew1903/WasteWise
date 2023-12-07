from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.cache import never_cache
from .models import donations

# Create your views here.
def index(request):
    return render(request,'index.html')

def signin(request):
    return render(request,'signin.html')

@never_cache
def register(request):
    
    if request.method=='POST':
        
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                messages.info(request,"user can't be registered \n")
                return redirect(('register'))
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                return redirect('signin')
        else:
            messages.info(request,"passwords doesn't match \n")
            return redirect('register')
                
    
    else:
        return render(request,'register.html')
        

@never_cache
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
            
        else:
            return redirect('login')
            
    else:
            return render(request,'login.html')
            

@never_cache
def logout(request):
    auth.logout(request)
    return redirect (('signin'))


@never_cache
def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        mobile=request.POST['mobile']
        food_type=request.POST['food_type']
        quantity=request.POST['quantity']
        address=request.POST['address']
        en=donations(name=name,mobile=mobile,food_type=food_type,quantity=quantity,address=address)
        en.save()
        return render(request,'contact.html')

    else:
        return render(request,'contact.html')



def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def order(request):
    return render(request,'order.html',{'data':donations.objects.all()})


