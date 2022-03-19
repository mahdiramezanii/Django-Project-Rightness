from django.db import models


class Home1_text(models.Model):
    text1=models.TextField()
    text2=models.TextField()
    text_box1=models.CharField(max_length=200)
    text_box12=models.CharField(max_length=200)


class Home1_item1(models.Model):
    item=models.CharField(max_length=200)

    def __str__(self):
        return self.item

class Home1_item2(models.Model):
    item1=models.CharField(max_length=50)
    item2=models.CharField(max_length=50)

    def __str__(self):

        return f"{self.item1[:5]} {self.item2[:5]}"


class content1(models.Model):

    titel=models.CharField(max_length=100)
    text=models.TextField()

    def __str__(self):

        return f"{self.titel[0:5]}  {self.text[:5]}"

class content2(models.Model):

    titel = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return f"{self.titel[0:5]}  {self.text[:5]}"

class content3(models.Model):
    titel = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return f"{self.titel[0:5]}  {self.text[:5]}"


class khadamat(models.Model):
    titel = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return f"{self.titel[0:5]}  {self.text[:5]}"


class profile_me(models.Model):

    image=models.ImageField(upload_to="content/profile/image",null=True,blank=True)
    name=models.CharField(max_length=50)
    mahart=models.CharField(max_length=50)
    about_me=models.TextField()
    fasebook=models.CharField(max_length=50)
    twiter=models.CharField(max_length=50)
    youtube=models.CharField(max_length=50)
    instagram=models.CharField(max_length=50)
