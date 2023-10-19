from django.db import models

# Create your models here.

# Blog author (logged-in user)
class Author(models.Model):
    # Fields
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200) # I don't think I want this to be changeable
    email = models.CharField(max_length=200, default=None)
    profile = models.TextField(blank = True)

    #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.name
    
    #def get_absolute_url(self):
    #    return reverse("my_blog", args=[str(self.id)])
    # Not sure if I need this

# Blog (for logged-in user)
class MyBlog(models.Model):
    # Fields
    name = models.CharField(max_length=200)
    # Need a one-to-many relationship with posts;
    # One blog has many posts

    #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.name
    
    #def get_absolute_url(self):
    #    return reverse("my_blog", args=[str(self.id)])
    # Not sure if I need this