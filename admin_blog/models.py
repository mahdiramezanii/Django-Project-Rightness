from django.db import models

# Create your models here.

class darkhast(models.Model):

    phone=models.CharField(max_length=20)
    text=models.TextField()
    how_to_send=models.CharField(max_length=20)


    def __str__(self):

        return self.phone