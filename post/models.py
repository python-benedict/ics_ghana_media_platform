from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.utils.text import slugify
from django.urls import reverse
import uuid

# Create your models here.

#This function will create a folder authomatically and send details of an individual user to one directory 
def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Tag(models.Model):
    title = models.CharField(max_length=100, verbose_name='tag')
    slug = models.SlugField(null=False, unique=True, default=uuid.uuid1)
    
    #this will make us see Tag if we have only one tag but Tags if we have more than one tag
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    
    #this will help you get all the post associated with the tag
    # def get_absolute_url(self):
    #     return reverse('tags', args=[self.slug])
    
    def __str__(self):
        return self.title
    
    #when saving if the slug doesn't match with the slugfield it should create one that matches it.
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.slug)
        return super().save(*args, **kwargs)
    

class Post(models.Model):
    #id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable=False)
    title = models.CharField(max_length=500, verbose_name="title", blank=True)
    picture = models.ImageField(upload_to=user_directory_path, verbose_name="Picture", null=True)
    caption = models.CharField(max_length=500000, verbose_name="Caption")
    posted = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag, related_name="tags")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    
    #this will help you get all the post associated with the id
    def get_absolute_url(self):
        return reverse('post-details', args=[str(self.id)])
    
    def __str__(self):
        return self.caption
    
   
class TreandingPost(models.Model):
    #id = models.UUIDField(primary_key = True, default = uuid.uuid4)
    title = models.CharField(max_length=500, verbose_name="title", blank=True)
    picture = models.ImageField(upload_to=user_directory_path, verbose_name="Picture", null=True)
    caption = models.CharField(max_length=500000, verbose_name="Caption")
    posted = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag, related_name="trendingPostTag")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    
    #this will help you get all the post associated with the id
    def get_absolute_url(self):
        return reverse('post-details', args=[str(self.id)])
    
    def __str__(self):
        return self.caption    


class LocalNews(models.Model):
    #id = models.UUIDField(primary_key = True, default = uuid.uuid4)
    title = models.CharField(max_length=500, verbose_name="title", blank=True)
    picture = models.ImageField(upload_to=user_directory_path, verbose_name="Picture", null=True)
    caption = models.CharField(max_length=500000, verbose_name="Caption")
    posted = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag, related_name="localnews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    
    #this will help you get all the post associated with the id
    def get_absolute_url(self):
        return reverse('post-details', args=[str(self.id)])
    
    def __str__(self):
        return self.caption    
    
    
class NewEvent(models.Model):
    #id = models.UUIDField(primary_key = True, default = uuid.uuid4)
    title = models.CharField(max_length=500, verbose_name="title", blank=True)
    picture = models.ImageField(upload_to=user_directory_path, verbose_name="Picture", null=True)
    caption = models.CharField(max_length=500000, verbose_name="Caption")
    posted = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag, related_name="newEvent")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    
    #this will help you get all the post associated with the id
    def get_absolute_url(self):
        return reverse('post-details', args=[str(self.id)])
    
    def __str__(self):
        return self.caption      
    

class InternationalNews(models.Model):
    #id = models.UUIDField(primary_key = True, default = uuid.uuid4)
    title = models.CharField(max_length=500, verbose_name="title", blank=True)
    picture = models.ImageField(upload_to=user_directory_path, verbose_name="Picture", null=True)
    caption = models.CharField(max_length=500000, verbose_name="Caption")
    posted = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag, related_name="internationalNews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    
    #this will help you get all the post associated with the id
    def get_absolute_url(self):
        return reverse('post-details', args=[str(self.id)])
    
    def __str__(self):
        return self.caption  
    
class TechnologicalNews(models.Model):
    title = models.CharField(max_length=500, verbose_name="title", blank=True)
    picture = models.ImageField(upload_to=user_directory_path, verbose_name="Picture", null=True)
    caption = models.CharField(max_length=500000, verbose_name="Caption")
    posted = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag, related_name="technologicalNews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    
    #this will help you get all the post associated with the id
    def get_absolute_url(self):
        return reverse('post-details', args=[str(self.id)])
    
    def __str__(self):
        return self.caption 


class Articles(models.Model):
    title = models.CharField(max_length=500, verbose_name="title", blank=True)
    picture = models.ImageField(upload_to=user_directory_path, verbose_name="Picture", null=True)
    caption = models.CharField(max_length=500000, verbose_name="Caption")
    posted = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag, related_name="article")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    
    #this will help you get all the post associated with the id
    def get_absolute_url(self):
        return reverse('post-details', args=[str(self.id)])
    
    def __str__(self):
        return self.title 


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    
class Stream(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stream_follower")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stream_user")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField()
    
    def add_post(sender, instance, *args, **kwargs):
        post = instance
        user = post.user
        followers = Follow.objects.all().filter(following=user)
        for follower in followers:
            stream = Stream(post=post, user=follower.follower, date=post.posted, following=user)
            stream.save()
            
post_save.connect(Stream.add_post, sender=Post)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
class InternationalNewsComment(models.Model):
    post = models.ForeignKey(InternationalNews, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
class TechnologicalNewsComment(models.Model):
    post = models.ForeignKey(TechnologicalNews, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
class LocalNewsComment(models.Model):
    post = models.ForeignKey(LocalNews, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
class ArticlesComment(models.Model):
    post = models.ForeignKey(Articles, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
class Profile(models.Model):
    about_me = models.TextField()
    image = models.ImageField(upload_to='profile_image', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
    