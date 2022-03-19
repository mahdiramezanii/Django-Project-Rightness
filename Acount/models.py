from django.db import models
from django.contrib.auth.models import User

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    father_name=models.CharField(max_length=50)
    nation_code=models.CharField(max_length=50)
    image=models.ImageField(default="defult/index.png",upload_to="profile_user",blank=True,null=True)


    def __str__(self):
        return self.nation_code
