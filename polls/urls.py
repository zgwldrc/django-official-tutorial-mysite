from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.QuestionDetailView.as_view(), name='question_detail'),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='question_vote'),
]
