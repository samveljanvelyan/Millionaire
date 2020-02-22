from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import MultipleChoiceQuestion, Answer

# Global variables are used to pass generated questions and received answers from start_the_game
# to game_result function.
QUESTIONS, ANSWERS = [], []


# Create your views here.


@login_required
def start_the_game(request):
    """View function for starting the game."""
    global QUESTIONS, ANSWERS

    # Querying a random 5 questions from database.
    questions = MultipleChoiceQuestion.objects.raw("""SELECT * FROM QA_multiplechoicequestion 
                                                  ORDER BY RANDOM() LIMIT 5""")

    questions_id = [questions[i].id for i in range(5)]
    # Getting respective answers for each question, using the questiions id.
    answers = [Answer.objects.get(question=answer_id) for answer_id in questions_id]
    QUESTIONS, ANSWERS = questions, answers
    return render(request, 'QA/gameplay.html', {'questions': questions,
                                                'answers': answers})


@login_required
def game_result(request):
    """View function for game results."""
    global QUESTIONS, ANSWERS

    points = 0
    first_name = request.user.first_name
    last_name = request.user.last_name
    questions, answers = QUESTIONS, ANSWERS

    # Setting global variables back to default values.
    QUESTIONS, ANSWERS = [], []

    # Getting user selected answers.
    selected_answers = request.POST.getlist('selections')

    correct_answers = [correct_ans.correct_answer for correct_ans in answers]

    # Adding respective points for each correctly answered question.
    for index, answer in enumerate(selected_answers):
        if selected_answers[index] == correct_answers[index]:
            points += questions[index].rank
    return render(request, 'QA/game_result.html', {'questions': questions,
                                                   'answers': answers,
                                                   'selected_answers': selected_answers,
                                                   'correct_answers': correct_answers,
                                                   'first_name': first_name,
                                                   'last_name': last_name,
                                                   'points': points
                                                   })


@login_required
def show_leader_board(request):
    """View function for showing the leader board."""
    return render(request, 'QA/leader_board.html')
