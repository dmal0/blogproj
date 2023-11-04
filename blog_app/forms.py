from django.forms import ModelForm
from .models import Post, Comment

# Create post form
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image')

# Create comment form
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('commenter', 'content')