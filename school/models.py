from django.db import models

# Create your models here.
class user(models.Model):
    username=models.CharField(max_length=300)
    password=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    role = models.CharField(max_length=10)
    otp = models.IntegerField(default=456)

    def __str__(self):
        return self.username


class Student(models.Model):
    user_id = models.ForeignKey(user,on_delete=models.CASCADE)
    username=models.CharField(max_length=300)
    password=models.CharField(max_length=200)
    email=models.EmailField(unique=True)

class Faculty(models.Model):
    user_id = models.ForeignKey(user,on_delete=models.CASCADE)
    username=models.CharField(max_length=300)
    password=models.CharField(max_length=200)
    email=models.EmailField(unique=True)

class counsellor(models.Model):
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    username=models.CharField(max_length=300)
    password=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
