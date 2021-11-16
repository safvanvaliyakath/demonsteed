from django.db import models

# Create your models here.

class listuser(models.Model):
    name=models.CharField(max_length=100,unique=True)
    desc=models.TextField()
    image=models.ImageField(upload_to='images')

    def __str__(self):
        return self.name