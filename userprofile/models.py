from django.db import models

from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .manager import CustomUserManager





class User(AbstractBaseUser , PermissionsMixin): # from step 2
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = "email"

    objects = CustomUserManager()
    
    def __str__(self):
        return self.email

class ProfilePage(models.Model):
    User = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 30,null = True)
    email = models.EmailField(max_length = 256, null = True,unique=True)
    profilephoto = models.ImageField(upload_to='images/',null = True , blank = True ,default = "default.jpg")
    no_of_followers = models.IntegerField(default = 0,null = True)
    no_of_following = models.IntegerField(default = 0,null = True)
    no_of_posts = models.IntegerField(default = 0,null = True)
    bio = models.CharField(max_length = 200 , null = True)

    def __str__(self):
        return self.email
    
        
class Posts(models.Model):
    uploader = models.ForeignKey(User,null = True , on_delete = models.CASCADE)
    img = models.ImageField(upload_to = 'images/',null = True)
    caption = models.CharField(max_length = 400 , null = True)
    time = models.DateTimeField(auto_now_add = True)
    Like = models.BooleanField(default = False)
    no_of_likes = models.IntegerField(default = 0)
    #comment
    def __str__(self):
        return self.caption
    
class LikePost(models.Model):
    user = models.ForeignKey(User,null = True ,on_delete = models.CASCADE)
    post = models.ForeignKey(Posts ,null = True ,on_delete = models.CASCADE)

    class Meta:
        unique_together = ('user','post')

class CommentOnPost(models.Model):
    user = models.ForeignKey(User, null = True , on_delete = models.CASCADE)
    post = models.ForeignKey(Posts,null = True , on_delete = models.CASCADE)
    description = models.CharField(max_length = 400, default = "commented")
    time = models.DateTimeField(auto_now_add = True)

    class Meta:
        unique_together = ('user','post','time')





class Followers(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE ,related_name = "follow_user")
    follower = models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        unique_together = ('user','follower')

