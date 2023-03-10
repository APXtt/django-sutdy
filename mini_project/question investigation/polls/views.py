from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.urls import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic

# generic View안쓸 떄
# def index(request):
#     lastest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         'lastest_question_list': lastest_question_list
#     }
#     return render(request, 'polls/index.html', context)

# generic View사용할 때
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'lastest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]
    


def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    context = {
        'question':question,
        'question_id':question_id,
    }
    return render(request, 'polls/detail.html', context)







def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question_id': question_id,
        'question': question,
    }
    return render(request, 'polls/result.html', context)







def vote(request, question_id):
    print('test')
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
            'question_id': question_id
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,))) # 두번 투표 방지