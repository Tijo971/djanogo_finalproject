from django.db import models
from Books.models import BookDB

# Create your models here.

class UserDB(models.Model):
    UserName = models.CharField(max_length=50, null=True, blank=True)
    EmailId = models.EmailField(max_length=50, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    PassWord = models.CharField(max_length=50, null=True, blank=True)
    UserImage = models.ImageField(upload_to="UserProfile", null=True, blank=True)


class CartDB(models.Model):
    Username = models.CharField(max_length=20, null=True, blank=True)
    pro_name = models.CharField(max_length=20, null=True, blank=True)
    aut_name = models.CharField(max_length=20, null=True, blank=True)
    Qty = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)



class Checkout(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    State = models.CharField(max_length=20, null=True, blank=True)
    zip = models.IntegerField(null=True, blank=True)
    c_name = models.CharField(max_length=20, null=True, blank=True)
    c_number = models.IntegerField(null=True, blank=True)
    exp_month = models.CharField(max_length=20, null=True, blank=True)
    exp_yer = models.IntegerField(null=True, blank=True)
    cvv = models.IntegerField(null=True, blank=True)


class Review(models.Model):
    user=models.CharField(max_length=20, null=True, blank=True)
    product=models.CharField(max_length=20, null=True, blank=True)
    comment=models.CharField(max_length=1000, null=True, blank=True)
    rate=models.IntegerField(default=0, null=True, blank=True)
    created_at=models.DateField(auto_now_add=True)




