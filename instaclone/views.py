from asyncio.windows_events import NULL
from itertools import chain
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.views.generic import CreateView,ListView
from django.contrib.auth.models import User
from account.forms import userInfoForm,userProfileForm
from account.models import posts,userInfo,FollowersCount
from account.models import PostVideo

# class indexView(ListView):
#     template_name = 'index.html'
#     model = posts
#     context_object_name = 'recentpost'
#     ordering = ['posted_at']
    
    
def IndexFeedView(req):
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
            return HttpResponseRedirect('account/login') 
        else:
            
            print(user_form.errors,profile_form.errors)
    
    else:
        user_form = userInfoForm()
        profile_form = userProfileForm()
        
        
    feed_list=[] 
    if req.user.username:
        user_object = User.objects.get(username = req.user.username)
        user_profile = userInfo.objects.get(user= user_object)
        user_following_list = []
        feed = []
        post = posts.objects.all()
        print("-------------------------- index page ----------------------")
        print(post)
        user_following = FollowersCount.objects.filter(follower = user_profile)
        for users in user_following:
            user_following_list.append(users.user)
            
        for usernames in user_following_list:
            feed_lists = posts.objects.filter(user= usernames)
            feed.append(feed_lists)
        feed_list = list(chain(*feed))
        
        
    feed_video_list =[]
    if req.user.username:
        user_object_video = User.objects.get(username = req.user.username)
        user_profile_video = userInfo.objects.get(user= user_object_video)
        user_following_list_video = []
        video_feed = []
        postv = PostVideo.objects.all()
        print(postv)
        print("-------------------------- video index page ----------------------")
        user_following_v = FollowersCount.objects.filter(follower = user_profile_video)
        for userv in user_following_v:
            user_following_list_video.append(userv.user)
            
        for usernames_v in user_following_list_video:
            feed_video_list = PostVideo.objects.filter(user= usernames_v)
            video_feed.append(feed_video_list)
        feed_video_list = list(chain(*video_feed))
    
    return render(req,'index.html',{'user_form':user_form,'registered':registered,'profile_form':profile_form,'feed_video_list':feed_video_list,'feed_list':feed_list})
    