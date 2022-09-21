
from django import forms
from account.models import userInfo
from django.contrib.auth.models import User

from account.models import posts
from account.models import FollowersCount
from account.models import PostComment, PostVideo

class userInfoForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password','label':'ghg'}))
    class Meta():
        model = User
        fields =('username','email','password')
        labels = {
            'username': '',
            'email':'',
            'password':'',
            
            
        }
        widgets={
            'username':forms.TextInput( attrs={'class':'form-control', 'placeholder':'username'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'email'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'})
        }
        

class userProfileForm(forms.ModelForm):
    class Meta():
        model = userInfo
        fields = ('bio',)
        labels = {
            'bio':'',
        }
        widgets={
            'bio':forms.Textarea(attrs={'class':'form-control','id':'textarea','placeholder':'bio(optional)',"rows":1, })
        }
 
class ImagePostForm(forms.ModelForm):
    user_post = forms.FileField(label_suffix=' ', label='upload post')
    class Meta():
        model = posts
        fields = ('user','user_post', 'caption')
        
        labels={
            'caption':'',
            # 'user_post':'upload post'
        }
        
        
        widgets={
            'user':forms.TextInput(attrs={'class':'form-control', 'id':'auth','value':'','type':'hidden'}),
            'caption':forms.Textarea(attrs={'class':'form-control','placeholder':'caption'}),
            
        }
        
class VideoPostForm(forms.ModelForm):
    class Meta():
        model = PostVideo
        fields = ('user','video_post','caption')   
        
        widgets={
                'user':forms.TextInput(attrs={'class':'form-control', 'id':'auth','value':'','type':'hidden'}),
                'caption':forms.Textarea(attrs={'class':'form-control','placeholder':'caption'}),
                
            }   
        labels={
            'caption':'',
            # 'user_post':'upload post'
        }
        
        
        
       
        
class PostUpdateForm(forms.ModelForm):
    class Meta():
        model = posts
        fields = ('user_post', 'caption')
        
        
        # widgets={
        #     'posted_at':forms.TextInput(attrs={'type':'hidden'}),
            
        # }

class ProfileUpdateFormOne(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username',)
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
        }
        
        
class ProfileUpdateFormTwo(forms.ModelForm):
    class Meta():
        model = userInfo
        fields = ('dp','bio',)
        widgets={
            'bio':forms.Textarea(attrs={'class':'form-control'}),
        }
        
        
# class UserFollowForm(forms.ModelForm):
#     class Meta():
#         model = FollowersCount
#         fields= ('follower','user')
#         widgets={
#             'follower':forms.TextInput(attrs={'class':'form-control', 'id':'follow','value':''}),
#             'user':forms.TextInput(attrs={'class':'form-control', 'id':'user','value':''}),
#         }


class PostCommentForm(forms.ModelForm):
    class Meta():
        model = PostComment
        fields = ("user", "comment_text","comment_on_post")
        labels = {
            'comment_text':''
        }
        
        widgets = {
            'user':forms.TextInput(attrs={'class':'form-control' ,'id':'commenter','value':'','type':'hidden'}),
            'comment_text':forms.Textarea(attrs={'class':'form-control' ,"rows":2,"cols" : 10, 'placeholder':'add comment..'}),
            'comment_on_post':forms.TextInput(attrs={'id':'post_id','value':'','type':'hidden'})
        }