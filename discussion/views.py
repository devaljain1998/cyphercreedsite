from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer, Vote
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import *
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from userprofile.models import Profile
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag
from dal import autocomplete
from actions.utils import create_action

# Create your views here.
def forum(request, tag_slug=None):
    question_list = Question.objects.filter(is_active=True)

    tag	=	None
    if	tag_slug:								
        tag	= get_object_or_404(Tag, slug=tag_slug)								
        question_list = question_list.filter(tags__in=[tag])

    #Pagination
    page = request.GET.get('page',1)
    paginator = Paginator(question_list, 5)

    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request,'discussion/forum.html',{'questions':questions,'tag':tag})

def questionView(request,pk):
    question = get_object_or_404(Question,pk=pk)
    answers = Answer.objects.filter(question=question.id)
    return render(request,'discussion/question_detail.html',{'question':question,'answers':answers})

@login_required
def question_form(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False) 
            question.user = request.user
            question.save()
            create_action(request.user, 'asked', question)
            form.save_m2m() #For django-taggit
            messages.success(request,'Success! Your Question has been added!')
            return redirect('forum')
        else:
            messages.error(request,form.errors)
    else:
        form = QuestionForm()
    return render(request,'discussion/question_form.html',{'form':form})  

@login_required
def add_answer(request, pk):
    ques = get_object_or_404(Question, pk = pk)
    if request.method == 'POST':
        form = AnswerForm(request.user,ques,request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            answer = form.save(commit=False)
            answer.question = ques
            answer.user = request.user
            answer.content = cd['content']
            answer.save()
            create_action(request.user, 'answered', ques)
            messages.success(request,'Success! Your Answer has been added!')
            return redirect('question_detail', pk=pk)
        else:
            messages.error(request,form.errors)
    else:
        form = AnswerForm(request.user,ques)
    return render(request,'discussion/answer_create.html',{'form':form})  

#Update Question:
@login_required
def edit_question(request, pk):
    question = get_object_or_404(Question,pk=pk)
    form = QuestionEditForm(instance=question)
    if request.method == 'POST':
        form = QuestionEditForm(request.POST,instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            create_action(request.user, 'edited', question)
            form.save_m2m() #For django-taggit
            return redirect('question_detail',pk=pk)
        else:
            messages.error(request,form.errors)
    return render(request,'discussion/question_edit.html',{'form':form,'question':question})

#Update Answer:
class AnswerUpdate(UpdateView,LoginRequiredMixin):
    model = Answer
    fields = ('content',)
    template_name = 'discussion/answer_update.html'

def edit_answer(request, ans_id):
    answer = get_object_or_404(Answer,pk=ans_id)
    question = answer.question
    form = AnswerForm(request.user, question, instance=answer)
    if request.method == 'POST':
        form = AnswerForm(request.user, question, request.POST,instance=answer)
        if form.is_valid():
            answer = form.save()
            #create_action(request.user,'edited answer:',answer)
            return redirect('question_detail',pk=question.id)
        else:
            messages.error(request,form.errors)
    return render(request,'discussion/answer_create.html',{'form':form})  

#Delete Question:
class QuestionDelete(DeleteView,LoginRequiredMixin):
    model = Question
    success_url = reverse_lazy('forum')

#Delete Answer:
#@login_required
class AnswerDelete(DeleteView,LoginRequiredMixin):
    model = Answer

    # def __init__(self,question,*args,**kwargs)
    #     super().__init__(*args,**kwargs)
    #     ques_id = self.request.question.id

    success_url =  reverse_lazy('forum') #reverse_lazy('question_detail',pk=self.question.id)

@login_required
def delete_answer(request,ans_id):
    answer = get_object_or_404(Answer,pk=ans_id)
    if request.method == 'POST': 
        ques_id = answer.question.id
        answer.delete()
        return redirect('question_detail',pk=ques_id)
    return render(request,'discussion/answer_confirm_delete.html',{'object':answer})



#Upvote View:
@login_required
def upvote(request, ans_id):
    answer = get_object_or_404(Answer,pk=ans_id)
    user = request.user
    alreadyVoted = Vote.objects.filter(user=user,answer=answer).first()
    if alreadyVoted is None:
        voted = Vote(user=user,answer=answer)
        voted.save()
        answer.upvotes += 1
        answer.save()
    return redirect('question_detail',pk=answer.question.id)

#Downvote View:
@login_required
def downvote(request, ans_id):
    answer = get_object_or_404(Answer,pk=ans_id)
    user = request.user
    alreadyVoted = Vote.objects.filter(user=user,answer=answer).first()
    if alreadyVoted is not None:
        alreadyVoted.delete()
        answer.upvotes -= 1
        if answer.upvotes < 0:
            answer.upvotes = 0
        answer.save()
    return redirect('question_detail', pk=answer.question.id)

#Accepted View:
@login_required
def accept_answer(request, ans_id):
    answer = get_object_or_404(Answer, pk=ans_id)
    answer.accepted = True
    answer.save()
    return redirect('question_detail',pk=answer.question.id)

#Add Comment View:
@login_required
def add_comment(request, ans_id, pk):
    answer = get_object_or_404(Answer, pk = ans_id)
    if request.method == 'POST':
        form = CommentForm(request.user, answer, request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            comment = form.save(commit=False)
            comment.answer = answer
            comment.user = request.user
            comment.content = cd['content']
            comment.save()
            messages.success(request,'Success! Your Comment has been posted!')
            return redirect('question_detail', pk=pk)
        else:
            messages.error(request,form.errors)
    else:
        form = CommentForm(request.user, answer)
    return render(request,'discussion/comment_create.html',{'form':form})  

class TagAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Tag.objects.none()

        qs = Tag.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


# I will deal with this later:
# class questionCreate(LoginRequiredMixin,CreateView):
#     form_class = QuestionForm 
#     template_name = 'discussion\question_form.html'

#     def get_initial(self):
#         return {'user':self.request.user.id}
#         #form_class.instance.user = User.objects.get(pk=self.request.user)

#     # def form_valid(self, form):
#     #     form.instance.user = User.objects.get(pk=self.request.user)
#     #     return super().form_valid(form)