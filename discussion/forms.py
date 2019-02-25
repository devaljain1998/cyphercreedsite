from .models import Answer, Question, Comment
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
    
    def __init__(self, author, question, *args, **kwargs):
        self.user = author
        self.question = question
        super().__init__(*args,**kwargs)

class QuestionEditForm(forms.ModelForm):
    #user = forms.ChoiceField(widget=forms.HiddenInput,disabled=True)
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea,help_text='Your question in detail. Note: MarkDown is enabled.')
    tags = TaggableManager()

    class Meta:
        model = Question
        fields = ['title','content','tags']

    # def __init__(self,author,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.user = author

    # def __init__(self,title,content,tags,*args,**kwargs):
    #     self.title = title
    #     self.content = content
    #     self.tags = tags
    #     super().__init__(*args,**kwargs)

class CommentForm(forms.Form):
    content = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'placeholder': 'Search'}))
    
    class Meta:
        model = Comment
        fields = ['content',]

    def __init__(self, author, answer, *args, **kwargs):
        self.answer = answer
        self.user = author
        super().__init__(*args, **kwargs)
