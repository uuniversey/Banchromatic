from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    path('questions/', views.question_list),
    path('questions/<int:question_pk>/', views.question_detail),
    path('updatereview/<int:article_pk>/', views.article_detail),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('articles/<int:article_pk>/comments/', views.comment_create),
    path('qa_comments/', views.qa_comment_list),
    path('qa_comments/<int:comment_pk>/', views.qa_comment_detail),
    path('qa_articles/<int:article_pk>/comments/', views.qa_comment_create),
]
