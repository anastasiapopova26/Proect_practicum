from django.contrib import admin

from polls.models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)
