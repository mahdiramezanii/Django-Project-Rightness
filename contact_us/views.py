from django.shortcuts import render
from .models import contactus,contact_by_me


def contact(request):

    context={
        "contact_me":contact_by_me.objects.all()
    }

    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        message=request.POST.get("message")
        contactus.objects.create(name=name,email=email,text=message)

    return render(request,"contact_us/contact-us.html",context)
