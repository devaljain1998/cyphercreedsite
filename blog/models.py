from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200,null=False,blank=False)
    content = models.TextField()
    published_date = models.DateField(default=timezone.now)
    AUTHOR_CHOICES = (
        ('Deval Sethi',"Deval Sethi"),
        ('Ujjwal Singh Bhadoria',"Ujjwal Singh Bhadoria"),
        ('Shishir Maurya',"Shishir Maurya"),
        ('Arghya Debnath',"Arghya Debnath"),
    )
    author = models.CharField(max_length=50,choices=AUTHOR_CHOICES,default='Deval Sethi') 
    
    def __str__(self):
        return f'{self.title} by {self.author} on {self.published_date}'

    class Meta:
        ordering = ('-published_date',)
