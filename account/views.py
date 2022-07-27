from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from account.forms import(  userProfileForm,
                          ImagePostForm,
                          userInfoForm,  
                          PostUpdateForm,
                          ProfileUpdateFormOne,
                          ProfileUpdateFormTwo,
                         
                          )


from .models import ( posts,
                     likePost,
                     userInfo,
                     FollowersCount)
from django.views.generic import (DetailView,
                                  DeleteView,
                                  UpdateView,
                                  )
from django.db import transaction
# Create your views here.


def signupView(req):
    registered = False
    if req.method == 'POST':
        user_form = userInfoForm(data=req.POST)
        profile_form = userProfileForm(req.POST, req.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'dp' in req.FILES:
                profile.dp = req.FILES['dp']     
            profile.save()           
            registered = True
            # return render(req, 'account/login.html')            
        else:
            print(user_form.errors,profile_form.errors)
    
    else:
        user_form = userInfoForm()
        profile_form = userProfileForm()
    return render(req, 'account/signup.html',{'user_form':user_form,'registered':registered,'profile_form':profile_form})


def loginView(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        email = req.POST.get('email')
        password = req.POST.get('password')
        
        user = authenticate(username=username,email=email,password=password)
        if user.is_active:
            login(req,user)       
            return HttpResponseRedirect('/')    
        else:
            print('not active')
    else:
        return render(req,'account/login.html')
            
@login_required 
def logoutView(req):
    logout(req)
    return HttpResponseRedirect('/')

@login_required
def imagePostView(req):
    
    if req.method == 'POST':
        post_form = ImagePostForm(req.POST,req.FILES)       
        if post_form.is_valid():            
            post_form.save()
            # print(new.user)
            # print("-----------------------------------saved------------------------------\ncurrent-user:",req.user,req.user.id)
            # print(post_form)
            # users = posts.objects.all()
            # for post in users:
            #     print(post.user_id)
            #     print(post.user)            
            return HttpResponseRedirect('/')
            
        else:
            print('not valid post')
            
    else:
        post_form = ImagePostForm()
    return render(req, 'account/posts_form.html',{'post_form':post_form})

"""'''TO POST THE IMAGE USING CBV'''

# class imagePostView(CreateView):
#     model = posts
#     form_class= ImagePostForm 
#     success_url = reverse_lazy("index")           
    
#     def form_valid(self, form ) :
#         form.instance.username = self.request.user
#         return super().form_valid(form)
    
"""
   

@login_required
def postLikeView(req):
    username = req.user.username
    post_id = req.GET.get('post_id')
    post= posts.objects.get(id = post_id)
    like_filt = likePost.objects.filter(post_id =post_id,username =username).first()
    if like_filt == None:
        new_like = likePost.objects.create(post_id=post_id,username=username)
        new_like.save()
        post.likes= post.likes+1
        post.save()
        return redirect('/')
    else:
        like_filt.delete()
        post.likes = post.likes-1
        post.save()
        return redirect('/')
    
#TO GET DETAILS ABOUT PERSON

# def ProfileDetailView(req, pk):
#     user_obj = User.objects.get(id= pk)
#     user_profile = userInfo.objects.get(user= user_obj)
#     user_posts = posts.objects.filter(user = pk)
#     user_post_length = len(user_posts)
#     follower = req.user.username
#     user = pk

#     if FollowerCount.objects.filter(follower=follower, user=user).first():
#         button_text = 'Unfollow'
#     else:
#         button_text = 'Follow'

#     user_followers = len(FollowerCount.objects.filter(user=pk))
#     user_following = len(FollowerCount.objects.filter(follower=pk))
    
#     return render(req, 'account/userInfo_detail.html',{'user_obj':user_obj,'user_profile':user_profile,'user_posts':user_posts,'user_post_length':user_post_length,
#                                                        'user_followers':user_followers,'user_following ':user_following ,'button_text':button_text})
    
    
class PostDetailView(DetailView):
    model = posts
   
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = posts
    success_url = reverse_lazy('index')
    
"""# class postDeleteView(LoginRequiredMixin ,UserPassesTestMixin, DeleteView):
#     model= posts
#     success_url = reverse_lazy('index')
    
#     def test_func(self) :
#         post = self.get_object()
#         if self.request.user == post.user:
#             return True
#         return False
     
'''update using FBV's'''
# @login_required
# def PostUpdateView(request):
#     if request.method == 'POST':
#         update_form = PostUpdateForm(request.FILES, request.POST)
        
#         if update_form.is_valid():
#             update_form.save()
#             return render(request, 'index.html')
            
#     else:
#         update_form = PostUpdateForm()
#     return render(request,'account/editpost.html',{'update_form':update_form})

'''update using CBV's '''
"""

class PostUpdateView(UpdateView):
    model = posts
    form_class = PostUpdateForm
    template_name= 'account/posts_update.html'
    success_url = reverse_lazy('index')
    
# class ProfileUpdateView(UpdateView):
#     model = userInfo
#     form_class= ProfileUpdateForm
#     template_name= 'account/userInfo_update.html'
#     success_url = reverse_lazy('index')
  
    
#NOT WORKING PROPERLY 
@login_required
def ProfileUpdateView(req,id=None):
    if req.method == 'POST':
        one_form = ProfileUpdateFormOne(req.POST,instance=req.user)
        two_form = ProfileUpdateFormTwo(req.POST, req.FILES, instance = req.user.Display)
        if one_form.is_valid() and two_form.is_valid():
            one_form.save()
            two_form.save()
            
            return redirect('index')
    else:
        one_form = ProfileUpdateFormOne(instance=req.user)
        two_form = ProfileUpdateFormTwo(instance = req.user.Display)
    
    return render(req, 'account/userInfo_update.html', {'one_form':one_form, 'two_form':two_form})
        

def ProfileDetailView(request,pk):
    user_object = User.objects.get(id=pk) 
    user_profile = userInfo.objects.get(user=user_object)
    user_posts = posts.objects.filter(user=pk)
    user_post_length = len(user_posts)
    current_user = request.GET.get('user')    
    user_followers = len(FollowersCount.objects.filter(user=user_profile))
    user_following = len(FollowersCount.objects.filter(follower=user_profile)) 
    user_followers_list = FollowersCount.objects.filter(user= user_profile)
   
    
    
          
    user_followers_list1 = []
    for i in user_followers_list:        
        print(i.user)
        user_followers_list1.append(i.follower_id)    
         

    
    is_follows_this_user = False
    for a in user_followers_list1:
        print(a,'=',request.user.id)        
        if request.user.id == a:
            is_follows_this_user = True
        
      
    context =    {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts': user_posts,
        'user_post_length': user_post_length,
        'current_user':current_user,
        'user_followers':user_followers,
        'user_following':user_following,
        'is_follows_this_user':is_follows_this_user,      
        'user_followers_list':user_followers_list
    
    }
    return render(request,'account/userInfo_detail.html', context)

def FollowersListView(request,pk):
    user_object = User.objects.get(id=pk)     
    user_profile = userInfo.objects.get(user=user_object)
    user_followers_list = FollowersCount.objects.filter(user=user_profile) 
    user_followers_list1 = []   
    for i in user_followers_list:
        user_followers_list = i.follower
        user_followers_list1.append(user_followers_list)
    return render(request,'account/followers.html',{'user_followers_list1':user_followers_list1,
                                                    'user_object':user_object,  
                                                                                                        
                                                    })
def FollowingListView(request,pk):
    user_object = User.objects.get(id=pk)     
    user_profile = userInfo.objects.get(user=user_object)
    following_list = FollowersCount.objects.filter(follower=user_profile)  
    following_list1 = []   
    for i in following_list:
        
        following_list1.append(i)
       
    return render(request,'account/following.html',{'user_object':user_object,'following_list1':following_list1,'user_profile':user_profile })
                

  
                    
    

@login_required
def follow(request):
    if request.method == 'POST': 
        follower = request.POST.get('follower')
        follower1 = userInfo.objects.get(pk= follower)  
        user  = request.POST.get('user')
        user1 = userInfo.objects.get(pk= user)
        print("-----------------------",user1)
        try:
            FollowersCount.objects.get(follower = follower1,user= user1)
            
        except Exception as e:
            follower_obj = FollowersCount.objects.create(follower = follower1,user= user1)
            follower_obj.save()
        return redirect(request.META.get('HTTP_REFERER'))       
        
        
    
@login_required
def unfollow(request):
    if request.method == 'POST': 
        follower = request.POST.get('unfollower')
        follower1 = userInfo.objects.get(pk= follower)  
        user  = request.POST.get('un_user')
        user1 = userInfo.objects.get(pk= user)     
        try:
            follower_obj = FollowersCount.objects.get(follower = follower1,user= user1)
            follower_obj.delete()            
        except Exception as e:
            pass
        return redirect(request.META.get('HTTP_REFERER'))
         