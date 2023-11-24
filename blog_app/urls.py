from django.urls import path, include
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
    #path('my/<int:pk>', views.myBlog, name='my_blog'),

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
    path('blog/<int:blog_id>/post/<int:pk>/comment/new', views.createComment, name='create_comment'),

    # Update comment on post
    path('blog/<int:blog_id>/post/<int:post_id>/comment/<int:pk>/edit', views.updateComment, name='update_comment'),

    # Delete comment on post
    path('blog/<int:blog_id>/post/<int:post_id>/comment/<int:pk>/delete', views.deleteComment, name='delete_comment'),

    ##################################################################################################
    # Management and settings
    ##################################################################################################

    # Path to logged-in user's post management page
    path('manage/<int:blog_id>', views.managePosts, name='manage_posts'),

    # Path to logged-in user's account settings
        # Final version ideally should work without blog_id
    path('settings/account/<int:author_id>', views.updateAccount, name='update_account'),

    # Path to logged-in user's account settings
        # Final version ideally should work without blog_id
    path('settings/blog/<int:blog_id>', views.updateBlog, name='update_blog'),

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

    ##################################################################################################
    # User accounts
    ##################################################################################################

    path('accounts/', include('django.contrib.auth.urls')),
    # Automatically maps:
    # accounts/ login/                      [name='login']
    # accounts/ logout/                     [name='logout']
    # accounts/ password_change/            [name='password_change']
    # accounts/ password_change/done/       [name='password_change_done']
    # accounts/ password_reset/             [name='password_reset']
    # accounts/ password_reset/done/        [name='password_reset_done']
    # accounts/ reset/<uidb64>/<token>/     [name='password_reset_complete']
    # accounts/ reset/done/

    # User registration
    path('accounts/register/', views.registerPage, name='register_page'),

    # Actual user page
    path('user/', views.userPage, name='user_page'),

]