from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from datetime import datetime
from django.urls.base import reverse
# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=100,blank=False,help_text='eg: Best tutorials on Django?')
    content = models.TextField(blank=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('question_detail',{'pk':self.id})

    class Meta:
        ordering = ('-created',)

class Answer(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE,blank=False)
    created = models.DateTimeField(auto_now_add=True)
    upvotes = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return '{}\'s Answer'.format(self.user.username)

    class Meta:
        	ordering = ('-upvotes','-created')

class Comment(models.Model):
    content = models.CharField(max_length=500, help_text = "Avoid comment like +1 or Thanks. Upvote to the answer instead" )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.created}'

    class Meta:
        	ordering = ('-created',)
    
