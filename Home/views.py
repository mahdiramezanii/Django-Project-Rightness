from django.shortcuts import render
from .models import Home1_item2,Home1_text,Home1_item1,content1,content2,content3,khadamat,profile_me
from blog.models import article
def Home(request):

    context={
        "text1":Home1_text.objects.all(),
        "item1":Home1_item1.objects.all(),
        "item2":Home1_item2.objects.all(),
        "content1":content1.objects.all(),
        "content2":content2.objects.all(),
        "content3":content3.objects.all(),
        "khadamat":khadamat.objects.all(),
        "profile":profile_me.objects.all(),
        "response":[],
        "article":article.objects.all()[0:3]
    }

    if request.method=="POST":
        vazn=request.POST.get("vazn")
        ghad=request.POST.get("ghad")
        sen=request.POST.get("sen")
        jensiat=request.POST.get("jensiat")

        bmi=float(vazn)/(float(ghad))**2
        bmi=float(bmi)
        print(vazn)

        if bmi < 18.5:
            context["response"].append("شما دارای کمبود وزن هستید")
        elif 18.5 <= bmi <= 24.5:
            context["response"].append("شما در سلامت کامل هستید")
        elif 25 <= bmi <= 29.9:
            context["response"].append("شما دارای اضافه وزن هستید")
        elif bmi >30:
            context["response"].append("شما دارای چاقی شدید هستید")

    return render(request,"Home/index.html",context)
