from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import profile
from django.conf import settings
from django.core.mail import send_mail
import random
import numpy
def user_login(request):

    if request.user.is_authenticated==True:
        return redirect("Home:Home")
    else:
        if request.method=="POST":
            username=request.POST.get("username")
            password=request.POST.get("password")

            user=authenticate(username=username,password=password)

            if user is not None:
                login(request,user)

                return redirect("Home:Home")




    return render(request,"Acount/login.html")

def user_logout(request):
    logout(request)
    return redirect("Home:Home")

def register(request):


    context={
        "errors":[]
    }

    if request.user.is_authenticated==True:
        return redirect("Home:Home")



    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        password2=request.POST.get("password2")

        if User.objects.filter(username=username).exists():
            context["errors"].append("نام کاربری از قبل وجود دارد")
            return render(request,"Acount/register.html",context)

        elif password != password2:
            context["errors"].append("رمز ها شباهت ندارد")

        elif User.objects.filter(email=email).exists():
            context["errors"].append("ایمیل از قبل وجود دارد")
            return render(request,"Acount/register.html",context)

        else:
            user=User.objects.create(username=username,password=password,email=email)
            user.set_password(password)
            user.save()

            subject = "به وبسایت من خوش آمدید"
            message = f"سلام {username} به وبسایت من خوشآمدی " \
                      f"من فرحناز هستم" \
                      f"امیدوارم باهم به جاخای خوبی برسیم"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail(subject, message, email_from, recipient_list)
            login(request,user)
            return redirect("Home:Home")


    return render(request,"Acount/register.html",context)


def change_pass(request):

    context={
        "errors":[],



    }

    number=numpy.random.randint(1,10,size=5)
    if request.method=="POST":
        email=request.POST.get("email")



        if User.objects.filter(email=email).exists():

            user=User.objects.get(email=email)
            subject = "تغییر رمز عبور"
            message = f"رمز تایید شما:{number}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail(subject, message, email_from, recipient_list)


            return render(request,"Acount/confuremail.html",context)

        else:
            context["errors"].append("نام كاربري وجود ندارد")
            return render(request,"Acount/change-password.html",context)

    if request.method=="POST":
            code=request.POST.get("code")
            print(code)
            if code==number:
                 return redirect("Acount:confirmation_Email")

    return render(request,"Acount/change-password.html")

def Email_confirmation(request):

    return render(request,"Acount/confuremail.html")