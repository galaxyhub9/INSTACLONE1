from itertools import chain
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.views.generic import CreateView,ListView
from django.contrib.auth.models import User
from account.forms import userInfoForm,userProfileForm
from account.models import posts,userInfo,FollowersCount

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
        
    if req.user.username:
        user_object = User.objects.get(username = req.user.username)
        user_profile = userInfo.objects.get(user= user_object)
        user_following_list = []
        feed = []
        post = posts.objects.all()
        user_following = FollowersCount.objects.filter(follower = user_profile)
        for users in user_following:
            user_following_list.append(users.user)
            
        for usernames in user_following_list:
            feed_lists = posts.objects.filter(user= usernames)
            feed.append(feed_lists)
        feed_list = list(chain(*feed))
        return render(req,'index.html',{'feed_list':feed_list})
    
    return render(req,'index.html',{'user_form':user_form,'registered':registered,'profile_form':profile_form})
    
    
def FirstView(req):
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
        return redirect('/')
            # return render(req, 'account/login.html')            
        # else:
            
        #     print(user_form.errors,profile_form.errors)
    
    else:
        user_form = userInfoForm()
        profile_form = userProfileForm()
    return render(req, 'index1.html',{'user_form':user_form,'registered':registered,'profile_form':profile_form})
# def FeedView(req,pk):
#     user_object = User.objects.get(id=pk)     
#     user_profile = userInfo.objects.get(user=user_object)
#     user_following_list = FollowersCount.objects.filter(follower= user_profile)
#     user_posts_list=[]
#     print("----feedview-----")
#     for i in user_following_list:              
#         # print(i.user)
#         user_posts = posts.objects.filter(user =i.user)
#         user_posts_list.append(user_posts)       
        
#     feed_list=[]
#     for a in user_posts_list:
#         for b in a:
#             print(b)
#             feed_list.append(b)
#     print(feed_list)
    
#     return render(req,'feed.html',{'feed_list':feed_list})