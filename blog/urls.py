from django.urls import path
from . import  views

app_name="blog"
urlpatterns=[
    path("blog",views.weblog,name="blog"),
    path("post_detail/<int:slug>",views.post_detail,name="post")
]