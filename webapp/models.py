from django.db import models

# Create your models here.

class SignUp(models.Model):

    full_name=models.CharField(max_length=45)
    email_id=models.CharField(max_length=45)
    about_me=models.CharField(max_length=100)
    password=models.CharField(max_length=20)
    mobile_number=models.CharField(max_length=15)
    gender=models.CharField(max_length=10)
    country=models.CharField(max_length=20)
    state=models.CharField(max_length=45)
    city=models.CharField(max_length=30)
    profile_image=models.ImageField(upload_to="pictures/profile_image/",null=True,blank=True)

    def __str__(self):
         return self.full_name