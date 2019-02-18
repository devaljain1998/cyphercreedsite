from django.urls import path
from . import views

urlpatterns = [
    path('forum/',views.forum,name='forum'),
    path('question/<pk>/question_detail/',views.questionView,name='question_detail'),
    path('question/add/',views.questionCreate.as_view(),name='add_question'),
]