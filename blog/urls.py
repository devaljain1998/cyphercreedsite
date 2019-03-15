from django.urls import path
from . import views

urlpatterns = [
    path('',views.PostListView.as_view(),name='homepage'),
    # path('',views.post_list,name='homepage'),
    path('adminBlog/',views.PostListView.as_view(),name='post_list'),
]