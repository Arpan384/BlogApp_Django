from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)  #small amount of text
    slug = models.SlugField()
    body = models.TextField()  #large amount of text
    date = models.DateTimeField(auto_now_add=True)  #auto fills the time when an instance is created
    thumb = models.ImageField(default="default.png", blank=True)
    #add in author later
    author = models.ForeignKey(User, default = None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):    #this is a model method
        # to show only first 50 characters of bady on the articles page, we define a method by ourself and call this in template page like 'article.snippet'  [not ike article.snippet()]
        return self.body[:50] + '...'