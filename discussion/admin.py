from django.contrib import admin
from .models import Question, Answer, Comment
# Register your models here.

#Questions and Answers are needed to be modified
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Comment)