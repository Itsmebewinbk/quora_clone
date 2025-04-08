from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),
    path('create-question/', views.create_question, name='create_question'),
    path('answer-question/<int:question_id>/', views.answer_question, name='answer_question'),
    path('like-answer/<int:answer_id>/', views.like_answer, name='like_answer'),
]