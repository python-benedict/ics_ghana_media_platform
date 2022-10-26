from django.contrib import admin
from post.models import Tag, Post, Follow, Stream, TreandingPost, NewEvent

# Register your models here.

admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(TreandingPost)
admin.site.register(NewEvent)
admin.site.register(Follow)
admin.site.register(Stream)