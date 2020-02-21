from typing import Generator

RECORDS_COUNT = 20

QUESTIONS, ANSWERS, CORRECT_ANSWERS, RANKS = [], [], [], []


def divide_chunks(given_list: list, size: int):
    """Divide the given list into evenly sliced chunks."""
    for i in range(0, len(given_list), size):
        yield given_list[i:i + size]


def get_question_chunks(file) -> Generator:
    """Performs chunks division on the file."""
    with open(file, 'r') as fh:
        return divide_chunks(fh.readlines(), 6)


def get_questions(file):
    """Gets questions and appends to global QUESTIONS list."""
    for question in get_question_chunks(file):
        QUESTIONS.append(question[0].rstrip())


def get_answers(file):
    """Gets answers and appends to global ANSWERS list."""
    for question in get_question_chunks(file):
        ANSWERS.append(
            [question[1].rstrip(), question[2].rstrip(),
             question[3].rstrip(), question[4].rstrip()])


def find_right_answer(answers):
    """Finds the index of correct answer."""
    for answer in answers:
        for index, item in enumerate(answer):
            if item.endswith("*"):
                CORRECT_ANSWERS.append(answer[index].rstrip("*"))


def clean_answers(answers):
    """Cleans the right answer from asterix."""
    for answer in answers:
        for index, item in enumerate(answer):
            if item.endswith("*"):
                answer[index] = item.rstrip("*")


def get_ranks(file):
    """Gets ranks and appends to global RANKS list."""
    for question in get_question_chunks(file):
        RANKS.append(int(question[-1].rstrip()))


def fill_global_variables(file):
    get_questions(file)
    get_answers(file)
    find_right_answer(ANSWERS)
    clean_answers(ANSWERS)
    get_ranks(file)
