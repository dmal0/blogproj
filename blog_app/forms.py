from django.forms import ModelForm
from .models import Post, Comment, Author, Blog

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
        fields = ('name', 'email', 'profile', 'image')

# Blog form
class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('name',)