from xml.etree.ElementTree import Comment
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Tag, Stream, Post, Follow, TreandingPost, NewEvent, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CommentForm, UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-posted')
    context = {
        'post_items' :  posts   
    }
    return render(request, "home.html", context)

#Home Detailed Post
def detail_page(request, id):
    

    #Comment form
    if request.method == 'POST':
        post = Post.objects.get(id=id)
        body = request.POST.get("body")
        commment = Comment.objects.create(post=post, user=request.user, body=body)
        print(commment.body)
 
    #Comment
    
    #detailed_page = get_object_or_404(Post, id=id)
    detailed_page = Post.objects.get(pk=id)
    comments = Comment.objects.filter(post=detailed_page).order_by('-date')
    form = CommentForm()
    
    context = {
        'detailed_page':detailed_page,
        'form':form,
        'comments': comments,
    }
    
    return render(request, 'detail_page.html', context)


#Trending post
def trending(request):
    trendingposts = TreandingPost.objects.all().order_by('-posted')
    context = {
        'trending_items' :  trendingposts   
    }
    return render(request, "trending.html", context)


#Trending Detailed Post
def trending_detailed_page(request, id):
    #trending_detail_page = get_object_or_404(TreandingPost, pk=id)
    trending_detail_page = TreandingPost.objects.get(pk=id)
    return render(request, 'trending_detail_page.html', {'trending_detailed_pages':trending_detail_page})


#New Event Post
def newEvent(request):
    newEvents = NewEvent.objects.all().order_by('-posted')
    context = {
        'newEvent_items' :  newEvents   
    }
    return render(request, "newevent.html", context)


#New Event Detailed Post
def detail_newEvent(request, id):
    #detailNewEventPage = get_object_or_404(NewEvent, pk=id)
    detailNewEventPage = NewEvent.objects.get(pk=id)
    return render(request, 'new_event_detailed_page.html', {'neventdetail':detailNewEventPage})

#Registration view

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)
