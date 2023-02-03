from django.db import models
from accounts.models import *
from django_mysql.models import ListCharField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import CharField
# Create your models here.
class Room(models.Model):
    ratings=models.IntegerField(null=True,blank=True,default=0,validators=[
                MaxValueValidator(5),
                MinValueValidator(0)
            ])
    preferred_tags=ListCharField(base_field=CharField(max_length=255),size=None,max_length=(255),blank=True,null=True)
    created_by=models.ForeignKey(MyUser,on_delete=models.CASCADE,null=True,blank=True)
    extra_details=models.TextField(null=True,blank=True)
    space=models.DecimalField(null=True, blank=True, decimal_places=4, max_digits=8)
    rent_cost=models.IntegerField(null=True, blank=True)
    panaroma_image=models.ImageField(null=True, blank=True,upload_to='images/')
    image1=models.ImageField(null=True, blank=True,upload_to='images/')
    image2=models.ImageField(null=True, blank=True,upload_to='images/')
    image3=models.ImageField(null=True, blank=True,upload_to='images/')
    image4=models.ImageField(null=True, blank=True,upload_to='images/')
    address=models.TextField(null=True, blank=True)
    locality=models.CharField(null=True, blank=True,max_length=255)
    city=models.CharField(null=True, blank=True,max_length=255)
    state=models.CharField(null=True, blank=True,max_length=255)
    zipcode=models.CharField(null=True, blank=True,max_length=255)
    is_booked=models.BooleanField(default=False)
    def __str__(self):
        return str(self.id)

class Post(models.Model):
    user_id = models.ForeignKey( MyUser, on_delete=models.DO_NOTHING)
    room_id = models.ForeignKey(Room, on_delete=models.DO_NOTHING)
    user_count = models.IntegerField(default=1,validators=[
                MaxValueValidator(4),
                MinValueValidator(1)
            ])
    post_description=models.TextField(null=True, blank=True)
    def __str__(self):
        return str(self.room_id)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user_id', 'room_id'], name='room_id&user_id'
            )
        ]

class Interested_Users(models.Model):
    user_id=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    room_id=models.ForeignKey(Room, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.room_id)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user_id', 'room_id'], name='interested_user'
            )
        ]


class Contact_Us(models.Model):
    room_id=models.ForeignKey(Room,on_delete=models.CASCADE,null=True,blank=True)
    email_subject=models.CharField(max_length=255)
    email_sender=models.EmailField(max_length=255,null=True,blank=True)
    email_receiver=models.EmailField(max_length=255,null=True,blank=True)
    email_body=models.TextField(null=True,blank=True)
    def __str__(self):
        return str(self.email_subject)