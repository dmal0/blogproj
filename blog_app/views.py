from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # Render index.html
    return render( request, 'blog_app/index.html')

# Logged-in user's own blog
def myBlog(request):
    # Render blog.html
    return render( request, 'blog_app/my_blog.html')

# Logged-in user's post management page
def managePosts(request):
    # Render relevant template
    return render( request, 'blog_app/manage_posts.html')

# Logged-in user's settings for account and blog
def settings(request):
    # Render relevant template
    return render( request, 'blog_app/settings.html')

# Logged-in user's saved blogs
def savedBlogs(request):
    # Render relevant template
    return render( request, 'blog_app/saved_blogs.html')