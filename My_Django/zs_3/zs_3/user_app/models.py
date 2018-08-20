from django.db import models

# Create your models here.
class Username(models.Model):
    user_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.user_name

class User(models.Model):
    u_name = models.ForeignKey(Username)
    f_name = models.CharField(max_length=264, unique=False)
    l_name = models.CharField(max_length=264, unique=False)

    def __str__(self):
        return self.l_name + ", " + self.f_name

class Email(models.Model):
    person = models.ForeignKey(User)
    u_email = models.EmailField(unique=True)

    def __str__(self):
        return(self.u_email)
