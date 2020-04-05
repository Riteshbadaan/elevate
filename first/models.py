from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.TextField(default=0)

    def __str__(self):
        return self.user.username

class userprofile2(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    game=models.TextField();


class teamdetails(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    typeofcompany=models.CharField(max_length=50)
    insti_name=models.CharField(max_length=50)
    pl1= models.CharField(max_length=50)
    phone1 = models.TextField(default=0)
    email1=models.TextField()
    pl2 = models.CharField(max_length=50)
    phone2 = models.TextField(default=0)
    email2 = models.TextField()
    pl3 = models.CharField(max_length=50)
    phone3 = models.TextField(default=0)
    email3 = models.TextField()
    pl4 = models.CharField(max_length=50)
    phone4 = models.TextField(default=0)
    email4 = models.TextField()
    pl5 = models.CharField(max_length=50)
    phone5 = models.TextField(default=0)
    email5 = models.TextField()
    pl6 = models.CharField(max_length=50)
    phone6 = models.TextField(default=0)
    email6 = models.TextField()
    pl7 = models.CharField(max_length=50)
    phone7 = models.TextField(default=0)
    email7 = models.TextField()
    pl8 = models.CharField(max_length=50)
    phone8 = models.TextField(default=0)
    email8 = models.TextField()
    pl9 = models.CharField(max_length=50)
    phone9 = models.TextField(default=0)
    email9 = models.TextField()
    pl10 = models.CharField(max_length=50)
    phone10 = models.TextField(default=0)
    email10 = models.TextField()
    pl11 = models.CharField(max_length=50)
    phone11 = models.TextField(default=0)
    email11 = models.TextField()
    pl12 = models.CharField(max_length=50)
    phone12 = models.TextField(default=0)
    email12 = models.TextField()














