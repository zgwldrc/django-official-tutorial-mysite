from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.QuestionDetailView.as_view(), name='question_detail'),
    path('<int:pk>/result/', views.ResultView.as_view(), name='question_result'),
    path('<int:question_id>/vote/', views.vote, name='question_vote'),
]
