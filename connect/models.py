from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    featured_img = models.ImageField(upload_to='profile_imgs/',null=True)



class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    caption = models.CharField(null=True,max_length=400)
    add_photos = models.ImageField(upload_to="post_imgs/",null=True)
    add_location = models.CharField(null=True,max_length=50)
    add_tags = models.CharField(null=True,max_length=50)

