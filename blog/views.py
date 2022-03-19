from django.shortcuts import render
from .models import article,categorical
from contact_us.models import contact_by_me
def weblog(request):
    context={
        "article":article.objects.all(),

    }

    return render(request,"blog/blog-default.html",context)



def post_detail(request,slug):

    context={
        "post":article.objects.get(slug=slug),
        "contact": contact_by_me.objects.all()
    }


    return render(request,"blog/post-details.html",context)