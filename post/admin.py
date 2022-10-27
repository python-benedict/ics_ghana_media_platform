from django.contrib import admin
from post.models import Tag, Post, Follow, Stream, TreandingPost, NewEvent, InternationalNews, Comment, Profile, TechnologicalNews, LocalNews, LocalNewsComment, TechnologicalNewsComment

# Register your models here.

admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(TreandingPost)
admin.site.register(NewEvent)
admin.site.register(InternationalNews)
admin.site.register(Follow)
admin.site.register(Stream)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(TechnologicalNews)
admin.site.register(TechnologicalNewsComment)
admin.site.register(LocalNews)
admin.site.register(LocalNewsComment)
