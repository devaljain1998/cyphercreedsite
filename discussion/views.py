from django.shortcuts import render, get_object_or_404
from .models import Question, Answer
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def forum(request):
    questions = Question.objects.filter(is_active=True)
    answered = []
    for question in questions:
        answered.append(Answer.objects.filter(question=question.id).count()) #Untested till now
    #Pagination
    return render(request,'discussion/forum.html',{'questions':questions,'answered':answered})

def questionView(request,pk):
    question = get_object_or_404(Question,pk=pk)
    answers = Answer.objects.filter(question=question.id)
    return render(request,'discussion/question_detail.html',{'question':question,'answers':answers})

class questionCreate(LoginRequiredMixin,CreateView):
    model = Question
    fields = '__all__'

class answerCreate(LoginRequiredMixin,CreateView):
    model = Answer
    fields = 'content'

    
