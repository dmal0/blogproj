from django.forms import ModelForm
from .models import Post, Comment, Author, Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Post form
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image')

# Comment form
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('commenter', 'content')

# Author form
class AuthorForm(ModelForm):
    class Meta:
        model = Author
        #removed "email" after "name"
        fields = ('name', 'profile', 'image')
        #exclude = ['user']

# Blog form
class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('name', 'theme')
        #exclude = ['user', 'author']

# Create User form
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')