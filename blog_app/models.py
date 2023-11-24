from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

# Blog author (logged-in user)
class Author(models.Model):
    # Fields
    name = models.CharField(max_length=200, default="Anonymous")
    username = models.CharField(max_length=200) # I don't think I want this to be changeable
    email = models.CharField(max_length=200, default=None)
    profile = models.TextField(blank = True)
    image = models.ImageField(upload_to="images/authors/", null=True, blank=True, default="")
    # Author relationship with user
    # https://stackoverflow.com/questions/39527289/associating-users-with-models-django
    #user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, unique=True)
    
    # One-to-One Blog-Author relationship; Author has one Blog, Blog has one Author
    #blog = models.OneToOneField(Blog, on_delete=models.CASCADE, unique=True, default = None)

    # Define default String to return the name for representing the Model object.
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("my_blog", args=[str(self.id)])
    # Not sure if I need this

# Blog (for logged-in user)
class Blog(models.Model):
    #List of choices for major value in database, human readable name
    THEME = (
        ('None', 'None'),
        ('BO', 'Blood Orange'),
        ('LL', 'Lemon Lime'),
    )

    # Fields
    name = models.CharField(max_length=200, default="Untitled")
    # One-to-One Blog-Author relationship; Author has one Blog, Blog has one Author
    author = models.OneToOneField(Author, on_delete=models.CASCADE, unique=True, default="Anonymous")
    # Same relationship for User
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, unique=True)
    # Custom color theme
    theme = models.CharField(max_length=200, choices=THEME, null=True, default=None)

    #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("blog-detail", args=[str(self.id)])
    # Not sure if I need this

# Blog Post
class Post(models.Model):
    title = models.CharField(max_length=100, default="", blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to="images/", null=True, blank=True, default="")
    
    # One-to-Many Blog-Post relationship; Blog has many Posts, Posts belong to one Blog
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, default=None, related_name='blogPosts')

    # Same relationship for User
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, default=None)
    
    # One-to-Many Author-Post relationship; Author has many Posts, Posts belong to one Author
    # Removed this so posts could be created; it was redundant because
    # posts belong to blogs, and blogs have authors
    #author = models.CharField(max_length=100, default="", blank=True)
    #author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None)
    
    # Define default String to return the name for representing the Model object.
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post-detail", args=[str(self.id)])
    
# Post Comment
class Comment(models.Model):
    # Post comment belongs to; One post has many comments
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)
    
    # General / if anonymous; ideally would like to attach blog authors if logged in
    commenter = models.CharField(max_length=100, default="Anonymous")
    
    # Actual comment content
    content = models.TextField()