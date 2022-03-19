from django.shortcuts import render
from blog.models import article


def admin_user(request):


    return render(request, "admin_blog/index.html")

def blog_coponents(request):

    context={
        "post":article.objects.all()
    }


    return render(request,"admin_blog/components-blog-posts.html",context)


def add_post(request):

    return render(request,"admin_blog/add-new-post.html")


def profile_blog(request):

    return render(request,"admin_blog/user-profile-lite.html")