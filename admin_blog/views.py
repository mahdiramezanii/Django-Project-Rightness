from django.shortcuts import render
from blog.models import article,categorical
from Acount.models import profile
from .models import darkhast
def admin_user(request):

    if request.method=="POST":

        phone=request.POST.get("phone")
        text=request.POST.get("text")
        v=request.POST.get("v")
        if phone and text:
            darkhast.objects.create(phone=phone,text=text,how_to_send=v)


    return render(request, "admin_blog/index.html")

def blog_coponents(request):

    context={
        "post":article.objects.all()
    }


    return render(request,"admin_blog/components-blog-posts.html",context)


def add_post(request):

    context={
        "categori":categorical.objects.all(),
        "errors":[]
    }

    if request.method=="POST":
        titel=request.POST.get("category")
        if categorical.objects.filter(titel=titel).exists():
            context["errors"].append("دسته بندی از قبل وجود دارد")
        else:
            if titel is not None:
                categorical.objects.create(titel=titel)
    if request.method=="POST":
        writer=request.user
        titel=request.POST.get("titel")
        categori=request.POST.get("categori")
        image=request.FILES.get("image")
        text=request.POST.get("text")
        if writer and titel and image and text and categori is not None:
            article.objects.create(witer=writer,titel=titel,image=image,text=text,categori=categori)



    return render(request,"admin_blog/add-new-post.html",context)


def profile_blog(request):
    user=request.user
    context={
        "p":profile.objects.get(user=user)
    }

    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        power=request.POST.get("power")
        password=request.POST.get("password")
        addres=request.POST.get("addres")
        discription=request.POST.get("discription")


        if profile.objects.get(user=user):

            profile.objects.update(first_name=first_name,last_name=last_name,email=email,power=power,password=password,addres=addres,discription=discription)



    return render(request,"admin_blog/user-profile-lite.html",context)