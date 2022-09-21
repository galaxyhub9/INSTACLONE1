
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date,time
from PIL import Image
# Create your models here.

class userInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='Display' ) # onetoone field is used bcoz we need only one user to have one profile ,if i use foreign key then i can make multiple profiles with single name which is not to be done
    dp = models.ImageField(upload_to='dp_images/%y/%m/%d',blank=True,default='static/user.png', null=True)
    bio = models.TextField(blank=True,null=True)
    joined_at =  models.DateField(auto_now=False,auto_now_add=True)

    def save(self) :
        super().save() 
        dp_img = Image.open(self.dp.path)
        if dp_img.height>300 or dp_img.width >300 :
            output = (300,300)
            dp_img.thumbnail(output)
            dp_img.save(self.dp.path)
        

    
    def __str__(self) :
        return self.user.username
     
class posts(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    user = models.ForeignKey(userInfo,on_delete=models.CASCADE)
    user_post = models.ImageField(upload_to = 'post_image/%y/%m/%d')
    caption = models.TextField(blank=True,null=True)
    posted_at = models.DateTimeField(default=datetime.now)
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user.user.username
    
    def save(self) :
        super().save() 
        post_img = Image.open(self.user_post.path)
        if post_img.height>500 or post_img.width >500 :
            output = (300,300)
            post_img.thumbnail(output)
            post_img.save(self.user_post.path)
    
   
    
    @property
    def posted_days(self):
        pdays = self.posted_at.date()
        # today= date.today()
        # ago = pdays - today
        return pdays
    
class PostVideo(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    user = models.ForeignKey(userInfo,on_delete=models.CASCADE)
    caption = models.TextField(blank=True,null=True)
    posted_at = models.DateTimeField(default=datetime.now)
    likes = models.IntegerField(default=0)
    video_post = models.FileField(upload_to='post_video/%y/%m/%d',verbose_name="video",default='null')
    
    
    def __str__(self):
        return  "{}| {}".format(self.user.user.username, self.caption)
    
class likePost(models.Model):
    username = models.CharField(max_length=100)
    post_id = models.CharField( max_length=500) # it was giving me error if i use uuid field when i liked the  post 
    
    def __str__(self):
        return self.username
    
    
class FollowersCount(models.Model):
    follower = models.ForeignKey(userInfo,on_delete=models.CASCADE, related_name='is_follower')
    user = models.ForeignKey(userInfo,on_delete=models.CASCADE,related_name='is_followed')
    
    def __str__(self):
        return self.user
    

class PostComment(models.Model):
    user = models.ForeignKey(userInfo, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.TextField(max_length=1000)
    comment_on_post =models.UUIDField()
    commented_date = models.DateTimeField(auto_now=datetime.now())
    
    def __str__(self) :
        return "{}   |  {}  | {}".format(self.user, self.comment_text, self.comment_on_post)