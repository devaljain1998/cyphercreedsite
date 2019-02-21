from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import QuestionForm, AnswerForm
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from userprofile.models import Profile

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

# I will deal with this later:
class questionCreate(LoginRequiredMixin,CreateView):
    form_class = QuestionForm 
    template_name = 'discussion\question_form.html'

    def get_initial(self):
        return {'user':self.request.user.id}
        #form_class.instance.user = User.objects.get(pk=self.request.user)

    # def form_valid(self, form):
    #     form.instance.user = User.objects.get(pk=self.request.user)
    #     return super().form_valid(form)

@login_required
def question_form(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            question = Question(title=cd['title'],content=cd['content'],user=request.user,tags=cd['tags'])
            question.save()
            messages.success(request,'Success! Your Question has been added!')
            return redirect('forum')
        else:
            messages.error(request,form.errors)
    else:
        form = QuestionForm()
    return render(request,'discussion/question_form.html',{'form':form})  

@login_required
def add_answer(request, pk):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            ques = get_object_or_404(Question, pk = pk)
            answer = Answer(content=cd['content'],user=request.user,question=ques)
            answer.save()
            messages.success(request,'Success! Your Answer has been added!')
            return redirect('question_detail' pk=pk)
        else:
            messages.error(request,form.errors)
    else:
        form = AnswerForm()
    return render(request,'discussion/answer_create.html',{'form':form})  

# class answerCreate(LoginRequiredMixin,CreateView):
#     form_class = AnswerForm
#     fields = 'content'
#     template_name = 'discussion/answer_create.html'

    
