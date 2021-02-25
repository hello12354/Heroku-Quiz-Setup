from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path(r'quiz', views.quiz, name='quiz'),
    path(r'recommendations', views.recommendations, name='recommendations'),
    url(r'submit', views.submit, name='submit'),
    url(r'startQuiz', views.quiz, name='startQuiz'),
    url(r'programs', views.programs, name='programs'),
    url(r'about', views.about, name='about'),
    url(r'emailSubmission', views.email, name='emailSubmit')

]
