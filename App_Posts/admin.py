from django.contrib import admin
from App_Posts.models import Post,Likes,Comment
# Register your models here.
admin.site.register(Post)
admin.site.register(Likes)
admin.site.register(Comment)