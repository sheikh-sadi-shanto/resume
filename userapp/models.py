from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save
import uuid
# Create your models here.
class Profile(models.Model):
    gander_choice=(('male','male'),('female','female'),('other','other'))
    
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_profile')
    pro_pic=models.ImageField(upload_to='pro_pic',null=True,blank=True,default='default.png')
    cover_pic=models.ImageField(upload_to='pic',null=True,blank=True,default='default.png')
    title=models.CharField(max_length=120,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    gander=models.CharField(choices=gander_choice,max_length=20,null=True,blank=True)
    number=models.IntegerField(null=True,blank=True)
    adress=models.CharField(max_length=100,null=True,blank=True)
    describtion=models.TextField(max_length=500,null=True,blank=True)
    
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwards):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance,created,**kwards):
    instance.user_profile.save()



class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=150)
    message=models.TextField(max_length=500)

class Post_user(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    user=models.CharField(max_length=25)
    caption=models.TextField()
    post_img=models.ImageField(upload_to='post_user')
    likes=models.IntegerField(default=0)
    created_at=models.DateTimeField(default=datetime.now)