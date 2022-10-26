from django.shortcuts import render, get_object_or_404
from .models import Tag, Stream, Post, Follow, TreandingPost, NewEvent
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-posted')
    context = {
        'post_items' :  posts   
    }
    return render(request, "home.html", context)

#Home Detailed Post
def detail_page(request, id):
    detailed_page = get_object_or_404(Post, pk=id)
    return render(request, 'detail_page.html', {'detailed_page':detailed_page})


#Trending post
def trending(request):
    trendingposts = TreandingPost.objects.all().order_by('-posted')
    context = {
        'trending_items' :  trendingposts   
    }
    return render(request, "trending.html", context)


#Trending Detailed Post
def trending_detailed_page(request, id):
    trending_detail_page = get_object_or_404(TreandingPost, pk=id)
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
    detailNewEventPage = get_object_or_404(NewEvent, pk=id)
    return render(request, 'new_event_detailed_page.html', {'neventdetail':detailNewEventPage})