from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50)
    discription = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    