from django.urls import path
from . import views

app_name="admin_blog"
urlpatterns=[
    path("admin_blog",views.admin_user,name="admin_blog"),
    path("blog_post",views.blog_coponents,name="blog_post"),
    path("add_post",views.add_post,name="add_post"),
    path("blog_profile",views.profile_blog,name="blog_profile")
]