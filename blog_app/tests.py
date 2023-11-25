from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog_app.models import Blog, Author, Post

# Blog detail view
class BlogDetailViewTest(TestCase):
    def setUp(self):
        # Create an author, blog, and post for testing
        self.user = User.objects.create(username='TestCaseUser', email='testcaseuser@uccs.edu', password1='abab1111', password2='abab1111')
        self.author = Author.objects.create(username=self.user.username, email=self.user.email)
        self.blog = Blog.objects.create()

    def test_portfolio_detail_view(self):
        # Test that the post detail view returns a 200 status code,
        # uses the correct template, and contains the post title
        response = self.client.get(reverse('portfolio-detail', args=[self.portfolio.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio_app/portfolio_detail.html')
        self.assertContains(response, 'test title')