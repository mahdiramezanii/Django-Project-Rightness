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
            message = f" سلام  {username} " \
                      f"به وبسایت من خوش اومدی" \
                      f"برای دریافت برنامه ورزشی وارد حساب کاربری خودت شو و فرم رو تکمیل کن" \
                      f"من برنامه روزنامه رو برات ارسال میکنم"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail(subject, message, email_from, recipient_list)

            subject2="ثبت نام جدید در سایت"
            message2=f"یک شخص جدید در سایت شما ثبت نام کرد" \
                      f": نام کاربری{username}" \
                      f":ایمیل{email}"
            email_from2 = settings.EMAIL_HOST_USER
            recipient_list2 = ["mahdiramazani1281@gmail.com", ]
            send_mail(subject2, message2, email_from2, recipient_list2)
            login(request,user)
            return redirect("Home:Home")


    return render(request,"Acount/register.html",context)


def change_pass(request):

    context={
        "errors":[],
    }


    if request.method=="POST":
        email=request.POST.get("email")
        pass1=request.POST.get("password1")
        pass2=request.POST.get("password2")

        if pass1 != pass2:
            context["errors"].append("رمز ها شباهن ندارد")
            return render(request, "Acount/change-password.html", context)

        if User.objects.filter(email=email).exists():

            user=User.objects.get(email=email)

            user.set_password(pass1)
            user.save()


            login(request,user)
            return redirect("Home:Home")

        else:
            context["errors"].append("ایمیل وجود ندارد")
            return render(request,"Acount/change-password.html",context)



    return render(request,"Acount/change-password.html")

