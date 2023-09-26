from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from userapp.form import Loginform,Registerform,Passchangeform,Profileform
from django.contrib import messages
from django.core.paginator import Paginator
from openpyxl import Workbook
from .models import Profile,Contact

# Create your views here.

def user_post(request):
    return render (request,'post.html')

def pro_edit(request):
    proform=Profileform()
    if request.method =='POST':
            # us.save()
            pass
    return render (request,'profileedit.html',{'proform':proform})

def profile(request):
    try:
        user_detail=User.objects.filter(username=request.user.username)
        profile_details=Profile.objects.filter(user=request.user)
        if request.method =='POST':
            pic=request.FILES.get('pro')
            cover=request.FILES.get('cover')
            eage=request.POST.get('eage')
            eemail=request.POST.get('eemail')
            enumber=request.POST.get('enumber')
            eaddress=request.POST.get('eaddress')
            edescribtion=request.POST.get('edescribtion')
            us=User.objects.get(username=request.user.username)
            us.email=eemail
            us.save()
            user1 = Profile.objects.get(user=us)
            if pic  ==None or  cover ==None:
                user1.age=eage
                user1.number=enumber
                user1.adress=eaddress
                user1.describtion=edescribtion
                if pic!=None:
                    user1.pro_pic=cover

                if cover!=None:
                    user1.cover_pic=pic
                user1.save()
                
            if pic  !=None or  cover !=None:
                user1.age=eage
                user1.number=enumber
                user1.adress=eaddress
                user1.describtion=edescribtion
                if pic !=None:
                    user1.pro_pic=pic
                if cover !=None:
                    user1.cover_pic=cover
                user1.save()
            

    except:
        profile_details=''
    return render(request,'profile.html',{'detail':profile_details,"user_detail":user_detail})

def home(request):
    all=User.objects.all()
    if request.method=='GET':
        a=request.GET.get("search")
        all=User.objects.filter(email=a)
    paginator = Paginator(all, 2)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'home.html',{'page_obj':page_obj})
    
def passchange(request):
    passform=Passchangeform(user=request.user)
    if request.method=="POST":
        passform=Passchangeform(user=request.user,data=request.POST)
        if passform.is_valid():
            messages.add_message(request,messages.INFO,'password change successful ')
            passform.save()
    return render(request,'passwordchange.html',{'passform':passform})

def loginview(request):
    if request.method=='POST':
        lform=Loginform(request.POST)
        if lform.is_valid():
            usern=lform.cleaned_data.get('username')
            pass1=lform.cleaned_data.get('password')
            print(usern,pass1)
            auth=authenticate(request,username=usern,password=pass1)
            if auth is not None:
                login(request,auth)
                print('login')
                return redirect('pro')
            else:
                print('fail')
    lform=Loginform()
    return render(request,'login.html',{'lform':lform})

def register(request):
    if request.method=='POST':
        rform=Registerform(request.POST)
        if rform.is_valid():
            messages.add_message(request,messages.INFO,'user creation successful ')
            rform.save()    
    else:
        rform=Registerform()
    return render(request,'register.html',{'rform':rform})

def log_out(request):
    logout(request)
    return redirect('login')



def sheikh(request):
    a=User.objects.filter(username='Sheikh_Sadi')
    all=Profile.objects.filter(id=4)
    if request.method =='POST':
        cname=request.POST.get('name')
        cemail=request.POST.get('email')
        cmessage=request.POST.get('message')
        Contact(name=cname,email=cemail,message=cmessage).save()
    return render(request,'sheikh.html',{'all':all,'a':a})
