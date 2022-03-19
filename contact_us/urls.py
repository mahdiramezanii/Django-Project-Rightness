from django.urls import path

from . import views
app_name="contact_us"
urlpatterns=[
    path("contact_us",views.contact,name="contact")
]