#rozne funkcje:
#wpisywanie:
#czasu
#id
#liczenie vote'ow
#wyswietlenia
#obrazek
#wszystko musi skladac i rozkladac z list/ w liste

import connection


def get_all_answers():
    a_list = connection.import_data('ask-mate-python/sample_data/answers.csv')
    return a_list


def get_questions():
    q_list = connection.import_data('ask-mate-python/sample_data/question.csv')
    return q_list


def one_question(id):
    questions = get_questions()
    id = int(id)
    question = questions[id]
    return question
