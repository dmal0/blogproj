from django.urls import path
from . import views

urlpatterns = [
    # path function defines a url pattern
    # '' is empty to represent based path to app
    # views.index is the function defined in views.py
    # name='index' parameter is to dynamically create url
    # example in html <a href="{% url 'index' %}">Home</a>.
    path('', views.index, name='index'),

    # Path to logged-in user's own blog
    path('blog', views.myBlog, name='my_blog'),

    # Path to any user's blog
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),

    # Path to any user's post
    #path('blog/<int:blog_id>/post/<int:post_id>', views.PostDetailView.as_view(), name='post'),

    #############################################################

    # Path to logged-in user's post management page
    path('manage', views.managePosts, name='manage_posts'),

    # Path to logged-in user's settings for their account and blog
    path('settings', views.settings, name='settings'),

    # Path to logged-in user's saved blogs
    path('saved', views.savedBlogs, name='savedBlogs'),
]