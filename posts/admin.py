from django.contrib import admin
from .models import Post,PostView,Comment

admin.site.register(Post)
admin.site.register(PostView)
admin.site.register(Comment)
