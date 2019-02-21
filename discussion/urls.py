from django.urls import path
from . import views

urlpatterns = [
    path('forum/',views.forum,name='forum'),
    path('question/<pk>/question_detail/',views.questionView,name='question_detail'),
    path('question/add/',views.question_form,name='add_question'),
    path('question/<pk>/question_detail/answer',views.add_answer,name='add_answer'),
    #path('question/<pk>/question_detail/answer',views.answerCreate.as_view(),name='add_answer'),
    #path('question/add/',views.questionCreate.as_view(),name='add_question'),
]