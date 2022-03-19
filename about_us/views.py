from django.shortcuts import render
from blog.models import article
def about(request):

    context={
        "article":article.objects.all()[0:3]
    }


    return render(request,"about_us/about-us.html",context)