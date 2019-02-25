from django.urls import path
from . import views

urlpatterns = [
    path('forum/',views.forum,name='forum'),
    path('question/<pk>/question_detail/',views.questionView,name='question_detail'),
    path('question/add/',views.question_form,name='add_question'),
    path('question/<pk>/question_detail/edit',views.edit_question,name='edit_question'),
    path('question/<pk>/question_detail/delete',views.QuestionDelete.as_view(),name='delete_question'),
    path('question/<pk>/question_detail/answer',views.add_answer,name='add_answer'),
    ##path('question/<pk>/question_detail/answer/edit',views.AnswerUpdate.as_view(),name='edit_answer'),
    path('question/<pk>/question_detail/answer/delete',views.AnswerDelete.as_view(),name='delete_answer'),

    #Cpath('question/<pk>/question_detail/answer/comment/success',views.add_comment,name='add_comment'),
    #path('question/<pk>/question_detail/answer/upvote/<ans_id>/success',views.upvote,name='answer_upvote'),
    path('upvote/<ans_id>/',views.upvote,name='answer_upvote'),
    path('downvote/<ans_id>/',views.downvote,name='answer_downvote'),
    path('accept_answer/<ans_id>/',views.accept_answer,name='accept_answer'),
    #path('question/<pk>/question_detail/answer/downvote/<ans_id>/success',views.downvote,name='answer_downvote'),
    
    #path('question/<pk>/question_detail/answer',views.answerCreate.as_view(),name='add_answer'),
    #path('question/add/',views.questionCreate.as_view(),name='add_question'),
]