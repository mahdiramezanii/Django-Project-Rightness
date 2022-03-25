from django.db import models
from django.contrib.auth.models import User

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    addres=models.TextField()
    discription=models.TextField()
    power=models.CharField(max_length=50,blank=True,null=True)
    image=models.ImageField(default="defult/index.png",upload_to="profile_user",null=True,blank=True)
    blog_admin=models.BooleanField(default=False)

    def __str__(self):
        return self.first_name
