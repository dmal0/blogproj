from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Author, Blog, Post

# Create your views here.

def index(request):
    # Render index.html
    return render( request, 'blog_app/index.html')

# Logged-in user's own blog
def myBlog(request):
    # Render blog.html
    return render( request, 'blog_app/my_blog.html')

##############################################

# Any user's blog
#def blog(request):
#    # Render blog.html
#    return render( request, 'blog_app/blog_detail.html')

# Any user's posts
class BlogDetailView(generic.DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = Post.objects.filter(blog=self.object)
        return context
    
#class PostDetailView(generic.DetailView):
#    model = Post
#
#    def post(request):
#        # Render actual post
#        return render( request, 'blog_app/post.html')

##############################################

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