from django.db import models

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=60)
    year=models.CharField(max_length=60)
    description=models.CharField(max_length=60)
    premium=models.BooleanField(default=False)
    image=models.ImageField(upload_to='images/posters',null=True,blank=True)

    def __str__(self):
        return self.title