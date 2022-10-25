from django.db import models
from django.contrib.auth.models import User
# from django.db.signals import post_save, post_delete
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
    def get_absolute_url(self):
        return reverse('tags', args=[self.slug])
    
    def __str__(self):
        return self.title
    
    #when saving if the slug doesn't match with the slugfield it should create one that matches it.
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.slug)
        return super().save(*args, **kwargs)