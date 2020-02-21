import os
import sqlite3
from sqlite3 import Error

from Millionaire.helpers import (fill_global_variables, RECORDS_COUNT, QUESTIONS,
                                 RANKS, ANSWERS, CORRECT_ANSWERS)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "db.sqlite3")
FILE_PATH = os.path.join(BASE_DIR, "questions.txt")


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def fill_db_with_questions_and_ranks(db_file):
    """Filling the database with questions and ranks from global variables."""
    connection = create_connection(db_file)
    cursor = connection.cursor()
    for index in range(RECORDS_COUNT):
        cursor.execute("""INSERT INTO QA_multiplechoicequestion(question, rank) VALUES(?, ?)""",
                       (QUESTIONS[index], RANKS[index]))
    connection.commit()
    connection.close()


def fill_db_with_answers(db_file):
    """Filling the database with answers and correct answers from global variables."""
    connection = create_connection(db_file)
    cursor = connection.cursor()
    for index in range(RECORDS_COUNT):
        cursor.execute("""INSERT INTO QA_answer(question_id, first_answer, second_answer, 
                                                third_answer, fourth_answer, correct_answer) 
                                                VALUES(?, ?, ?, ?, ?, ?)""",
                       (index + 1, ANSWERS[index][0], ANSWERS[index][1], ANSWERS[index][2],
                        ANSWERS[index][3], CORRECT_ANSWERS[index]))
    connection.commit()
    connection.close()


def run():
    fill_global_variables(FILE_PATH)
    fill_db_with_questions_and_ranks(DATABASE)
    fill_db_with_answers(DATABASE)


if __name__ == "__main__":
    run()
