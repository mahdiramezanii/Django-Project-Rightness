from django.urls import path
from . import views

app_name="about_us"
urlpatterns=[
    path("about_us",views.about,name="about")
]