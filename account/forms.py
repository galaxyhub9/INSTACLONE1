
from pyexpat import model
from attr import fields
from django import forms
from account.models import userInfo
from django.contrib.auth.models import User

from account.models import posts
from account.models import FollowersCount

class userInfoForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields =('username','email','password')
        

class userProfileForm(forms.ModelForm):
    class Meta():
        model = userInfo
        fields = ('dp', 'bio')
 
class ImagePostForm(forms.ModelForm):
    class Meta():
        model = posts
        fields = ('user','user_post', 'caption')
        
        
        widgets={
            'user':forms.TextInput(attrs={'class':'form-control', 'id':'auth','value':'','type':'hidden'}),
            'caption':forms.TextInput(attrs={'class':'form-control',}),
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
        
class ProfileUpdateFormTwo(forms.ModelForm):
    class Meta():
        model = userInfo
        fields = ('dp', 'bio')
        
# class UserFollowForm(forms.ModelForm):
#     class Meta():
#         model = FollowersCount
#         fields= ('follower','user')
#         widgets={
#             'follower':forms.TextInput(attrs={'class':'form-control', 'id':'follow','value':''}),
#             'user':forms.TextInput(attrs={'class':'form-control', 'id':'user','value':''}),
#         }