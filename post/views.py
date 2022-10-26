from django.shortcuts import render, get_object_or_404
from .models import Tag, Stream, Post, Follow
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-posted')
    context = {
        'post_items' :  posts
        
    }

    return render(request, "home.html", context)

def detail_page(request, id):
    detailed_page = get_object_or_404(Post, pk=id)
    return render(request, 'detail_page.html', {'detailed_page':detailed_page})

