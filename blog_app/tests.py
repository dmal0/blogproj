from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog_app.models import Blog, Author, Post, Comment
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

##################################################################################################
# Unit tests
##################################################################################################

class AuthorModelTest(TestCase):
    def setUp(self):
        # Create an author, blog, and post for testing
        self.user = User.objects.create(username='TestCaseUser', email='testcaseuser@uccs.edu')
        self.author = Author.objects.create(name=self.user.username,username=self.user.username, email=self.user.email)

    def test_author_str(self):
        # Test that the _str_ method returns the username and email of the user
        self.assertEqual(str(self.author.username), 'TestCaseUser')
        self.assertEqual(str(self.author.email), 'testcaseuser@uccs.edu')

class BlogModelTest(TestCase):
    def setUp(self):
        # Create an author, blog, and post for testing
        self.user = User.objects.create(username='TestCaseUser', email='testcaseuser@uccs.edu')
        self.author = Author.objects.create(name=self.user.username,username=self.user.username, email=self.user.email)
        self.blog = Blog.objects.create(name='Test Blog Title', author=self.author, user=self.user)

    def test_blog_str(self):
        # Test that the _str_ method returns the title of the blog and author
        self.assertEqual(str(self.blog.name), 'Test Blog Title')
        self.assertEqual(str(self.blog.author.username), 'TestCaseUser')

class PostModelTest(TestCase):
    def setUp(self):
        # Create an author, blog, and post for testing
        self.user = User.objects.create(username='TestCaseUser', email='testcaseuser@uccs.edu')
        self.author = Author.objects.create(name=self.user.username,username=self.user.username, email=self.user.email)
        self.blog = Blog.objects.create(name='Test Blog Title', author=self.author, user=self.user)
        self.post = Post.objects.create(title='Test Post Title', blog=self.blog, user=self.user)

    def test_post_str(self):
        # Test that the _str_ method returns the title of the post, blog name, and author
        self.assertEqual(str(self.post), 'Test Post Title')
        self.assertEqual(str(self.post.blog), 'Test Blog Title')
        self.assertEqual(str(self.post.blog.author.name), 'TestCaseUser')

class CommentModelTest(TestCase):
    def setUp(self):
        # Create an author, blog, and post for testing
        self.user = User.objects.create(username='TestCaseUser', email='testcaseuser@uccs.edu')
        self.author = Author.objects.create(name=self.user.username,username=self.user.username, email=self.user.email)
        self.blog = Blog.objects.create(name='Test Blog Title', author=self.author, user=self.user)
        self.post = Post.objects.create(title='Test Post Title', blog=self.blog, user=self.user)
        self.comment = Comment.objects.create(post=self.post, commenter='Test Commenter', content='This is a test comment')

    def test_comment_str(self):
        # Test that the _str_ method returns the title of the post, commenter, and content
        self.assertEqual(str(self.comment.post), 'Test Post Title')
        self.assertEqual(str(self.comment.commenter), 'Test Commenter')
        self.assertEqual(str(self.comment.content), 'This is a test comment')

##################################################################################################
# Selenium tests
##################################################################################################

class RegistrationFormTest(TestCase):
    def testform(self):
        selenium = webdriver.Firefox()
        # Visit URL
        selenium.get('http://127.0.0.1:8000/accounts/register')
        
        # Find elements for form submission
        user_un = selenium.find_element(By.ID,'id_username')
        user_em = selenium.find_element(By.ID,'id_email')
        user_pw1 = selenium.find_element(By.ID,'id_password1')
        user_pw2 = selenium.find_element(By.ID,'id_password2')

        submit = selenium.find_element(By.ID,'submit_create_user')

        # Populate form
        user_un.send_keys('TestCaseUserReg')
        user_em.send_keys('testcaseuserreg@uccs.edu')
        user_pw1.send_keys('ab12cd34')
        user_pw2.send_keys('ab12cd34')

        # Submit form
        submit.send_keys(Keys.RETURN)
        
        # Check All Blogs List
        selenium.get('http://127.0.0.1:8000/blogs')
        # Refresh the page
        time.sleep(5)
        selenium.refresh()
        allBlogs = selenium.page_source

        assert "TestCaseUserReg" in allBlogs

        #selenium.quit()

class LoginFormTest(TestCase):
    def testform(self):
        selenium = webdriver.Firefox()
        # Visit URL
        selenium.get('http://127.0.0.1:8000/accounts/login')
        
        # Find elements for form submission
        user_un = selenium.find_element(By.ID,'id_username')
        user_pw = selenium.find_element(By.ID,'id_password')

        submit = selenium.find_element(By.ID,'submit_login')

        # Populate form
        user_un.send_keys('TestCaseUser')
        user_pw.send_keys('ab12cd34')

        # Submit form
        submit.send_keys(Keys.RETURN)

        # Check Dashboard, which is only available to logged-in users
        time.sleep(5)
        selenium.get('http://127.0.0.1:8000/dashboard')
        dashboard = selenium.page_source

        assert "Dashboard" in dashboard

        #selenium.quit()

##################################################################################################
# Integration tests
##################################################################################################

# Blog detail view OK
class BlogDetailViewTest(TestCase):
    def setUp(self):
        # Create an author, blog, and post for testing
        self.user = User.objects.create(username='TestCaseUser', email='testcaseuser@uccs.edu')
        self.author = Author.objects.create(username=self.user.username, email=self.user.email)
        self.blog = Blog.objects.create(name='Test Blog Title', author=self.author, user=self.user)

    def test_blog_detail_view(self):
        # Test that the post detail view returns a 200 status code,
        # uses the correct template, and contains the blog title
        response = self.client.get(reverse('blog-detail', args=[self.user.blog.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_app/blog_detail.html')
        self.assertContains(response, 'Test Blog Title')

# All Blogs view OK
class AllBlogsViewTest(TestCase):
    def setUp(self):
        # Create an author, blog, and post for testing
        self.user = User.objects.create(username='TestCaseUser', email='testcaseuser@uccs.edu')
        self.author = Author.objects.create(username=self.user.username, email=self.user.email)
        self.blog = Blog.objects.create(name='Test Blog Title', author=self.author, user=self.user)

    def test_all_blogs_view(self):
        # Test that the post detail view returns a 200 status code,
        # uses the correct template, and contains the post title
        response = self.client.get(reverse('allBlogs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_app/all_blogs.html')
        self.assertContains(response, 'Test Blog Title') # Test blog should be in list

# All Comments view OK
class AllCommentsViewTest(TestCase):
    def setUp(self):
        # Create an author, blog, and post for testing
        self.user = User.objects.create(username='TestCaseUser', email='testcaseuser@uccs.edu')
        self.author = Author.objects.create(username=self.user.username, email=self.user.email)
        self.blog = Blog.objects.create(name='Test Blog Title', author=self.author, user=self.user)

    def test_all_comments_view(self):
        # Test that the all comments view returns a 200 status code,
        # uses the correct template, and contains the message for there being no comments
        response = self.client.get(reverse('allComments'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_app/all_comments.html')
        self.assertContains(response, 'no') # There should be no comments