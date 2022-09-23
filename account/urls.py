from django.urls import path

from account import views

app_name = 'account'

urlpatterns =[
    
    path('signup/',views.signupView,name='signup'),
    
    path('login/',views.loginView,name='login'),
    
    path('logout/',views.logoutView,name='logout'),    

    path('uploadpost/',views.imagePostView,name='uploadimage'),    
    
    path('uploadvideo/',views.VideoPostView,name='uploadvideo'),    
    
    path('profile/<int:pk>/',views.ProfileDetailView,name='profile-detail-view'),
    
    path('profile/updateprofile',views.ProfileUpdateView,name='profile-update-view'),

    path('postdetail/<pk>/',views.PostDetailView.as_view(),name='post-detail-view'),

    path('postdetail/<pk>/update',views.PostUpdateView.as_view(),name='post-update-view'), 
    
    path('postdetail/<id>/comment/',views.PostCommentView,name='comment'),
    
    path('postdetail/<id>/commentv/',views.PostCommentView,name='comment2'),

    path('postdetail/<pk>/delete/',views.PostDeleteView.as_view(),name='post-delete-view'),
    
    path('follower-list/<pk>',views.FollowersListView,name="followers_list"),
    
    path('following-list/<pk>',views.FollowingListView,name="following_list"),
    
    path('profile/<pk>/delete/',views.AccountDeleteView.as_view(),name='account-delete'),
    
    path('contact/',views.contactView,name='contact'),
    
    path('about/',views.aboutView,name='about'),
        
]

