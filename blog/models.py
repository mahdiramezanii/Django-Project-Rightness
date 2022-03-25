from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

from django.utils import timezone
class categorical(models.Model):
    titel=models.CharField(max_length=20)


    def __str__(self):

        return self.titel

class article(models.Model):

    witer=models.ForeignKey(User,on_delete=models.CASCADE)
    categori=models.CharField(max_length=20,default="test")
    titel=models.CharField(max_length=50)
    image=models.ImageField(upload_to="blog/image")
    text=models.TextField()
    #slug=models.SlugField(blank=True)
    create=models.DateField(default=timezone.now())

    def get_absulot_url(self):

        return reverse("blog:post",kwargs={"slug":self.id})


    def __str__(self):
        return self.titel

    """def save(self,*args,**kwargs):
        self.slug=slugify(self.titel)

        super(article, self).save(args,kwargs)"""



    class Meta:

        ordering=("-create",)