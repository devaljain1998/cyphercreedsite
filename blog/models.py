from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200,null=False,blank=False)
    content = models.TextField()
    published_date = models.DateField(default=timezone.now)
    AUTHOR_CHOICES = (
        (1,"Deval Sethi"),
        (2,"Ujjwal Singh Bhadoria"),
        (3,"Shishir Maurya"),
        (4,"Arghya Debnath"),
    )
    author = models.CharField(max_length=50,choices=AUTHOR_CHOICES,default=1) 
    
    def __str__(self):
        return f'{{self.title}} by {{self.author.value}} on {{self.published_date}}'