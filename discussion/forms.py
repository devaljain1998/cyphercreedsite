from .models import Answer, Question
from django import forms
from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth import get_user_model

class QuestionForm(forms.ModelForm):
    #user = forms.IntegerField(widget=forms.HiddenInput,disabled=True) #choices=get_user_model().objects.all(),
    title = forms.CharField(max_length=100,help_text='eg: Best tutorials on Django?')
    content = forms.CharField(widget=forms.Textarea,help_text='Your question in detail. Note: MarkDown is enabled.')
    tags = TaggableManager()

    class Meta:
        model = Question
        fields = ['title','content','tags',]

class AnswerForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea,help_text='Your Answer in Detail. Note: MarkDown is enabled.')
    
    class Meta:
        model = Answer
        fields = ['content'] 
    
    def __init__(self,author,question,*args,**kwargs):
        self.user = author
        self.question = question
        super().__init__(*args,**kwargs)
