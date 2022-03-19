from django.urls import path
from . import views
app_name="Acount"
urlpatterns=[
    path("login",views.user_login,name="login"),
    path("logout",views.user_logout,name="logout"),
    path("register",views.register,name="register"),
    path("change_pass",views.change_pass,name="change"),
    path("change_pass/confirmation",views.Email_confirmation,name="confirmation_Email")


]