from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import MultipleChoiceQuestion, Answer


# Create your views here.


@login_required
def start_the_game(request):
    if request.user.is_authenticated:
        username = request.user.username
    questions = MultipleChoiceQuestion.objects.raw("""SELECT * FROM QA_multiplechoicequestion 
                                                  ORDER BY RANDOM() LIMIT 5""")
    questions_id = [questions[i].id for i in range(5)]
    answers = [Answer.objects.get(question=answer_id) for answer_id in questions_id]
    return render(request, 'QA/gameplay.html', {'username': username,
                                                'questions': questions,
                                                'answers': answers})
