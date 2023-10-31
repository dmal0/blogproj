from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from .models import Author, Blog, Post
from .forms import PostForm

# Create your views here.

def index(request):
    # Render index.html
    return render( request, 'blog_app/index.html')

    #author_blogs = Author.objects.select_related('blog').all()
    #print("All blogs query set", author_blogs)
    #return render( request, 'blog_app/index.html', {'author_blogs':author_blogs})

# Dashboard
def dashboard(request):
    # Render dashboard.html
    return render( request, 'blog_app/dashboard.html')

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

##############################################

#class PostDetailView(generic.DetailView):
#    model = Post
#
#    def post(request):
#        # Render actual post
#        return render( request, 'blog_app/post.html')

# Create Post
def createPost(request, blog_id):
    form = PostForm()
    blog = Blog.objects.get(pk=blog_id)
    
    if request.method == 'POST':
        # Create a new dictionary with form data and blog_id
        post_data = request.POST.copy()
        post_data['blog_id'] = blog_id
        post_data['author_id'] = Blog.author_id
        # !!!!!!!!!! ADD AUTHOR ID !!!!!!!!!!
        
        form = PostForm(post_data)
        if form.is_valid():
            # Save the form without committing to the database
            post = form.save(commit=False)
            # Set the portfolio relationship
            post.blog = blog
            post.save()

            # Redirect back to the portfolio detail page
            return redirect('blog-detail', blog_id)

    context = {'form': form}
    return render(request, 'blog_app/post_form.html', context)

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

# All blogs
def allBlogs(request):
    # Render relevant template
    #return render( request, 'blog_app/all_blogs.html')

    author_blogs = Author.objects.select_related('blog').all()
    print("All blogs query set", author_blogs)
    return render( request, 'blog_app/all_blogs.html', {'author_blogs':author_blogs})