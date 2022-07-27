
from django.contrib import admin

from account.models import userInfo,posts,likePost,FollowersCount
from . import models
# Register your models here.

admin.site.register(userInfo)
admin.site.register(posts)
admin.site.register(likePost)
admin.site.register(FollowersCount)