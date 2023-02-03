from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django_mysql.models import ListCharField
from django.db.models import CharField
# Create your models here.
class MyUser(AbstractUser):
    user_id           = models.AutoField(primary_key=True)
    username          = models.CharField(max_length=50,unique=True,blank=False)
    first_name        = models.CharField(max_length=50,blank=False)
    last_name         = models.CharField(max_length=50,blank=False)
    email             = models.EmailField(max_length=100,unique=True)
    bio               = models.TextField(null=True, blank=True)
    dob               = models.DateField(null=True, blank=True)
    profile_pic       = models.ImageField(upload_to='images/',default='default.jpg') 
    is_landlord       = models.BooleanField(default=False)
    created_at        = models.DateTimeField(auto_now_add=True)
    is_verified       = models.BooleanField(default=False)
    interests         = ListCharField(base_field=CharField(max_length=255),size=None,max_length=(255),blank=True,null=True)
    is_active         = models.BooleanField(default=False)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']
    
    def __str__(self):
        return self.username

@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance = None, created = False, **kwargs):
    if created:
        token=Token.objects.create(user = instance)


class KYC_User(models.Model):
    user_id=models.OneToOneField(MyUser,on_delete=models.CASCADE,null=True,blank=True)
    document=models.ImageField(upload_to ='documents/')
    user_image=models.FileField(upload_to='photos/')
