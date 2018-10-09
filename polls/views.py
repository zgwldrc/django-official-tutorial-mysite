
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView
from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

class IndexView(ListView):
    model = Question

    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now(),
        ).order_by('-pub_date')[:10]


class QuestionDetailView(DetailView):
    model = Question

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


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

def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/result.html", {"question": question})

class ResultView(DetailView):
    model = Question
    template_name = "polls/question_result.html"



