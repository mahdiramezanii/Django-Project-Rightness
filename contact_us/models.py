from django.db import models

class contactus(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    text=models.TextField()


    def __str__(self):

        return f"{self.name} {self.text[:5]}"

class contact_by_me(models.Model):

    phone=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    email=models.EmailField()
