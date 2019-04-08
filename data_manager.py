#rozne funkcje:
#wpisywanie:
#czasu
#id
#liczenie vote'ow
#wyswietlenia
#obrazek
#wszystko musi skladac i rozkladac z list/ w liste

import connection
import datetime

def get_all_answers():
    a_list = connection.import_data('ask-mate-python/sample_data/answer.csv')
    return a_list

def get_questions():
    questions = connection.import_data('ask-mate-python/sample_data/question.csv')
    return questions

def add_answer(form_data, id):
    answers = connection.import_data('answers.csv')
    data = datetime.now()
    data = str(data)
    last_id = data_manager.get_questions()
    last_id = last_id[-1]['id']
    if int(last_id) > -1:
        new_id = int(last_id) + 1
    else:
        new_id = 0

    new_answer = {
        'id': new_id,
        'submission_time': data,
        'vote_number': 0,
        'question_id': id,
        'message': form_data['answer'],
        'image': None
    }
    answers.append(new_answer)
    connection.write_file(answers, 'answers.csv')