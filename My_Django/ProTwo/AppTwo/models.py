from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=264,unique=False)
    last_name = models.CharField(max_length=264,unique=False)
    email = models.EmailField(unique=True)

    def __str__(self):
        return "N: " + self.first_name + " " + self.last_name
