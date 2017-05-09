from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Question, Choice


class IndexView(ListView):
    model = Question


class QuestionDetailView(DetailView):
    model = Question


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/question_detail.html', {
            'question': question,
            'error_message': "Need a choice before vote!",
        })
    else:
        choice.votes += 1
        choice.save()
        return HttpResponseRedirect(reverse('polls:question_detail', args=(question_id,)))



