from django.db import models

# Create your models here.
class CategoryDB(models.Model):
    c_name=models.CharField(max_length=20, null=True, blank=True)
    c_description=models.CharField(max_length=20, null=True, blank=True)
    c_img=models.ImageField(upload_to='category', null=True, blank=True)

class BookDB(models.Model):
    b_category=models.CharField(max_length=20, null=True, blank=True)
    b_name=models.CharField(max_length=20, null=True, blank=True)
    b_price=models.IntegerField(null=True, blank=True)
    b_description=models.CharField(max_length=1000, null=True, blank=True)
    b_auther=models.CharField(max_length=20, null=True, blank=True)
    b_auth_desc=models.CharField(max_length=1000, null=True, blank=True)
    b_cover=models.ImageField(upload_to='Books', null=True, blank=True)

class UpcomeBk(models.Model):
    bk_nme=models.CharField(max_length=20, null=True, blank=True)
    bk_des=models.CharField(max_length=500, null=True, blank=True)
    bk_cov=models.ImageField(upload_to='upcomebk', null=True, blank=True)
