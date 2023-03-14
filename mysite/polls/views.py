from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Question

# Create your views here.
def index(request):
    all_questions = Question.objects.all()
    return render(request, 'polls/index.html', context={"all_questions": all_questions})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    return HttpResponse("You are looking at the results of question %s" % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s" % question_id)
