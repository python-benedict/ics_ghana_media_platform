from xml.etree.ElementTree import Comment
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Tag, Stream, Post, Follow, TreandingPost, NewEvent, Comment, User, Profile, InternationalNews, InternationalNewsComment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CommentForm, UserRegistrationForm, EditProfileForm, InternationalNewsCommentForm
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



# Create your views here.
def internationalnews(request):
    posts = InternationalNews.objects.all().order_by('-posted')
    context = {
        'post_items' :  posts   
    }
    return render(request, "internationalnews.html", context)


#Home Detailed Post
def InternationNewsDetailedPage(request, id):   
    #Comment form
    if request.method == 'POST':
        post = InternationalNews.objects.get(id=id)
        body = request.POST.get("body")
        commment = InternationalNewsComment.objects.create(post=post, user=request.user, body=body)
        print(commment.body)
    
    #detailed_page = get_object_or_404(Post, id=id)
    detailed_page = InternationalNews.objects.get(pk=id)
    comments = InternationalNewsComment.objects.filter(post=detailed_page).order_by('-date')
    form = InternationalNewsCommentForm()
    
    context = {
        'detailed_page':detailed_page,
        'form':form,
        'comments': comments,
    }   
    return render(request, 'int_detail_page.html', context)







#Trending post
def trending(request):
    trendingposts = TreandingPost.objects.all().order_by('-posted')
    context = {
        'trending_items' :  trendingposts   
    }
    return render(request, "trending.html", context)


#Trending Detailed Post
def trending_detailed_page(request, id):
    trending_detail_page = TreandingPost.objects.get(id=id)
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
    detailNewEventPage = NewEvent.objects.get(id=id)
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


#User profile page view
@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'profile.html', {'profile': profile, 'user': user})


#Edit user profile page view
@login_required
def edit_profile(request):
    if request.method == "POST":
        # request.user.username is the original username
        form = EditProfileForm(request.user.username, request.POST, request.FILES)
        if form.is_valid():
            about_me = form.cleaned_data["about_me"]
            username = form.cleaned_data["username"]
            image = form.cleaned_data["image"]

            user = User.objects.get(id=request.user.id)
            profile = Profile.objects.get(user=user)
            user.username = username
            user.save()
            profile.about_me = about_me
            if image:
                profile.image = image
            profile.save()
            return redirect("profile", username=user.username)
    else:
        form = EditProfileForm(request.user.username)
    return render(request, "edit_profile.html", {'form': form})



