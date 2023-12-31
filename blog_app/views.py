from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from .models import Author, Blog, Post, Comment
from .forms import PostForm, CommentForm, AuthorForm, BlogForm, CreateUserForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users

# Create your views here.

############################################################################################
# Dashboard and index
############################################################################################

# Index
def index(request):
    if request.user.is_authenticated:
        return render( request, 'blog_app/dashboard.html')
    else:
        # Render index.html
        return render( request, 'blog_app/index.html')

# Dashboard
@login_required(login_url='login')
#@allowed_users(allowed_roles='author_role')
def dashboard(request):
    # Comments list
    comment_list = Comment.objects.all().order_by('-id')[:3]  # Reverse newest order; only show up to 3
    #userBlog = request.user.blog.id
    #userPosts = Post.objects.filter(blog_id=userBlog)
    print("All comments query set: ", comment_list)

    # Blogs list
    blog_list = Blog.objects.all()[:5] # Only show up to 5
    print("All blogs query set: ", blog_list)

    # Render dashboard.html
    return render( request, 'blog_app/dashboard.html', {'comment_list':comment_list,'blog_list':blog_list})

############################################################################################
# Blog viewing
############################################################################################

# Logged-in user's own blog
#def myBlog(request, account):
    ## Render blog.html
    #return render( request, 'blog_app/my_blog.html')

# Any user's posts
class BlogDetailView(generic.DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = Post.objects.filter(blog=self.object).order_by('-id') # Reverse newest order
        return context

############################################################################################
# Post viewing
############################################################################################

class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_list'] = Comment.objects.filter(post=self.object)
        return context

############################################################################################
# Post CRUD
############################################################################################

# Create Post
    # Only the owner (Author) of a Blog should be able to make
    # posts on that Blog
@login_required(login_url='login')
def createPost(request, blog_id):
    form = PostForm(request.POST, request.FILES)
    blog = Blog.objects.get(pk=blog_id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        
        ## Create a new dictionary with form data and blog_id and author_id
        #post_data = request.POST.copy()
        #post_data['blog_id'] = blog_id
        
        #form = PostForm(post_data)
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

# Update Post
    # Only the owner (Author) of the Blog to which the Post belongs should be
    # able to update/edit the posts on that Blog
@login_required(login_url='login')
def updatePost(request, blog_id, pk):
    post = Post.objects.get(pk=pk)
    form = PostForm(request.POST or None, instance=post)

    if request.method == 'POST':
        if form.is_valid():
            form = PostForm(request.POST, request.FILES, instance=post)
            form.save()

            return redirect('post-detail', blog_id, pk)
        
    context = {'form': form}
    return render(request, 'blog_app/update_post.html', context)

# Delete Post
    # Only the owner (Author) of the Blog to which the Post belongs should be
    # able to delete the posts on that Blog
@login_required(login_url='login')
def deletePost(request, blog_id, pk):
    post = Post.objects.get(pk=pk)
    
    if request.method == 'POST':
        post.delete()

        # Redirect back to the blog detail page
        return redirect('blog-detail', blog_id)

    context = {'post': post}
    return render(request, 'blog_app/delete_post.html', context)

############################################################################################
# Comment CRUD
############################################################################################

# Create Comment
def createComment(request, blog_id, pk):
    form = CommentForm()
    post_id = Post.objects.get(pk=pk)  

    if request.method == 'POST':
        # Create a new dictionary with form data and post_id
        comment_data = request.POST.copy()
        comment_data['post_id'] = post_id
        
        form = CommentForm(comment_data)
        if form.is_valid():
            # Save the form without committing to the database
            comment = form.save(commit=False)
            # Set the post relationship
            comment.post = post_id
            comment.save()

            # Redirect back to the post detail page
            return redirect('post-detail', blog_id, pk)

    context = {'form': form}
    return render(request, 'blog_app/comment_form.html', context)

# Update Comment
    # Comments should not be able to be edited unless the user is logged in
    # Then, the comment would ideally be associated with their author ID
    # Commenters should only be able to update/edit their own comments
@login_required(login_url='login')
def updateComment(request, blog_id, post_id, pk):
    comment = Comment.objects.get(pk=pk)
    form = CommentForm(request.POST or None, instance=comment)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect('post-detail', blog_id, post_id)
        
    context = {'form': form}
    return render(request, 'blog_app/update_comment.html', context)

# Delete Comment
    # Comments should not be able to be edited unless the user is logged in
    # Blog owners (Authors) should be able to delete any comment;
    # Non-Blog owners should only be able to delete their own comments
@login_required(login_url='login')
def deleteComment(request, blog_id, post_id, pk):
    comment = Comment.objects.get(pk=pk)
    
    if request.method == 'POST':
        comment.delete()

        # Redirect back to the post detail page
        return redirect('post-detail', blog_id, post_id)

    context = {'comment': comment}
    return render(request, 'blog_app/delete_comment.html', context)

############################################################################################
# Management and settings
############################################################################################

# Logged-in user's post management page
@login_required(login_url='login')
def managePosts(request, blog_id):
    # Render relevant template
    #return render( request, 'blog_app/manage_posts.html')

    # TEMP - Only goes to Blog 1 (Loe's Blog) for Sprint 1
    post_list = Post.objects.filter(blog_id=blog_id).order_by('-id')
    print("All posts query set: ", post_list)

    # Render dashboard.html
    return render( request, 'blog_app/manage_posts.html', {'post_list':post_list})

# Logged-in user's account settings
@login_required(login_url='login')
def updateAccount(request, author_id):
    # Render relevant template
    #return render( request, 'blog_app/update_account.html')

    author = Author.objects.get(pk=author_id)
    form = AuthorForm(request.POST or None, instance=author)

    if request.method == 'POST':
        if form.is_valid():
            form = AuthorForm(request.POST, request.FILES, instance=author)
            form.save()

            return redirect('index')
        
    context = {'form': form}
    return render(request, 'blog_app/update_account.html', context)

# Logged-in user's blog settings
@login_required(login_url='login')
def updateBlog(request, blog_id):
    # Render relevant template
    #return render( request, 'blog_app/update_blog.html')
    
    blog = Blog.objects.get(pk=blog_id)
    form = BlogForm(request.POST or None, instance=blog)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect('index')
        
    context = {'form': form}
    return render(request, 'blog_app/update_blog.html', context)

############################################################################################
# Blog and comment lists
############################################################################################

# Logged-in user's saved blogs
@login_required(login_url='login')
def savedBlogs(request):
    # Render relevant template
    return render( request, 'blog_app/saved_blogs.html')

# All blogs
def allBlogs(request):
    # Blogs list
    blog_list = Blog.objects.all()
    print("All blogs query set: ", blog_list)

    # Render all_blogs.html
    return render( request, 'blog_app/all_blogs.html', {'blog_list':blog_list})

# All comments
def allComments(request):
    # Comments list
    comment_list = Comment.objects.all().order_by('-id') # Reverse newest order
    print("All comments query set: ", comment_list)

    # Render all_comments.html
    return render( request, 'blog_app/all_comments.html', {'comment_list':comment_list})

# All posts
def allPosts(request):
    # Posts list
    post_list = Post.objects.all().order_by('-id')
    print("All posts query set: ", post_list)

    # Render all_posts.html
    return render( request, 'blog_app/all_posts.html', {'post_list':post_list})

############################################################################################
# User accounts
############################################################################################

# User registration page
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            usr = form.save()
            # Get username and email
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            # Add user to group
            # https://stackoverflow.com/questions/66491021/doesnotexist-getting-group-matching-query-does-not-exist-error-while-saving
            #group = Group.objects.get_or_create(name='author_role')
            #usr.groups.add(group)

            # Set information
            author = Author.objects.create(name=username, username=username, email=email) # use author model
            blog = Blog.objects.create(author=author,user=usr) # use blog model
            blog.author = author
            blog.save()

            messages.success(request, 'Account created for ' + username)
            return redirect('login')
        
    context = {'form':form}
    return render(request, 'registration/register.html', context)

# User view
@login_required(login_url='login')
# Add allowed_users
def userPage(request):
    blog = request.user.blog
    form = BlogForm(instance = blog)
    print('Blog: ', blog)
    author = blog.author
    print('Author: ', author)

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
    
    context = {'authors':author, 'form':form}
    return render(request, 'blog_app/user.html', context)

# Dashboard redirect from /accounts/profile/
@login_required(login_url='login')
def dashboardRedirect(request):
    return render( request, 'blog_app/dashboard.html')