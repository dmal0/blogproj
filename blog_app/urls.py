from django.urls import path
from . import views

urlpatterns = [
    ##################################################################################################
    # Index and dashboard
    ##################################################################################################

    # path function defines a url pattern
    # '' is empty to represent based path to app
    # views.index is the function defined in views.py
    # name='index' parameter is to dynamically create url
    # example in html <a href="{% url 'index' %}">Home</a>.
    path('', views.index, name='index'),

    # Path to dashboard
    path('dashboard', views.dashboard, name='dashboard'),

    ##################################################################################################
    # Blog Detail viewing
    ##################################################################################################

    # Path to logged-in user's own blog
    path('blog', views.myBlog, name='my_blog'),

    # Path to any user's blog
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),

    ##################################################################################################
    # Post Detail viewing + CRUD
    ##################################################################################################

    # View details for any user's post
    path('blog/<int:blog_id>/post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),

    # Create new post
    path('blog/<int:blog_id>/new_post', views.createPost, name='create_post'),

    # Update (edit) post
    path('blog/<int:blog_id>/post/<int:pk>/edit', views.updatePost, name='update_post'),

    # Delete post
    path('blog/<int:blog_id>/post/<int:pk>/delete', views.deletePost, name='delete_post'),

    ##################################################################################################
    # Comment CRUD
    ##################################################################################################

    # Create new comment on a post
    path('blog/<int:blog_id>/post/<int:pk>/new_comment', views.createComment, name='create_comment'),

    # Update comment on post
    path('blog/<int:blog_id>/post/<int:post_id>/update_comment/<int:pk>', views.updateComment, name='update_comment'),

    # Delete comment on post
    path('blog/<int:blog_id>/post/<int:post_id>/delete_comment/<int:pk>', views.deleteComment, name='delete_comment'),

    ##################################################################################################
    # Management and settings
    ##################################################################################################

    # Path to logged-in user's post management page
    path('manage', views.managePosts, name='manage_posts'),

    # Path to logged-in user's settings for their account and blog
    path('settings', views.settings, name='settings'),

    ##################################################################################################
    # Blog and comment lists
    ##################################################################################################

    # Path to logged-in user's saved blogs
    path('saved', views.savedBlogs, name='savedBlogs'),

    # Path to all blogs
    path('blogs', views.allBlogs, name='allBlogs'),

    # Path to all comments
    path('comments', views.allComments, name='allComments'),

    # Path to all posts
    path('posts', views.allPosts, name='allPosts'),
]