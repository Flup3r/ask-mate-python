#rozne funkcje:
#wpisywanie:
#czasu
#id
#liczenie vote'ow
#wyswietlenia
#obrazek
#wszystko musi skladac i rozkladac z list/ w liste

import connection
import uuid
from datetime import datetime
import os


def get_all_answers():
    a_list = connection.import_data('ask-mate-python/sample_data/answer.csv')
    return a_list


def get_questions():
    q_list = connection.import_data('ask-mate-python/sample_data/question.csv')
    return q_list


def add_answer(form_data, id):
    answers = connection.import_data('ask-mate-python/sample_data/answer.csv')
    new_answer = {
        'id': uuid.uuid4(),
        'submission_time': datetime.now(),
        'vote_number': 0,
        'question_id': id,
        'message': form_data['answer'],
        'image': None
    }
    answers.append(new_answer)
    connection.write_file(answers, 'ask-mate-python/sample_data/answer.csv')


def one_question(id):
    questions = get_questions()
    for question in questions:
        if question['id'] == id:
            return question


def get_answers_to_question(id):
    id = id
    answers = get_all_answers()
    filtered_answers = []
    for answer in answers:
        if answer['question_id'] == id:
            filtered_answers.append(answer)
    return filtered_answers


def delete_element(element_type, element_id):
    # delete file if exists
    data = connection.import_data(f'ask-mate-python/sample_data/{element_type}.csv')
    try:
        deleted_element_img_path = [element['image'] for element in data if element['id'] == element_id][0]
        file_name = deleted_element_img_path.split("/")[1]
    except IndexError:
        pass

    # delete element
    updated_data = [data_element for data_element in data if data_element['id'] != element_id]
    connection.write_file(updated_data, f'ask-mate-python/sample_data/{element_type}.csv')

    answers = []
    if element_type == "question":
        answers = connection.import_data('ask-mate-python/sample_data/answer.csv')

        # delete answer's image
        img_paths_of_deleted_answers = [answer['image'] for answer in answers if answer['question_id'] == element_id]


        # delete answer
        updated_answers = [answer for answer in answers if answer['question_id'] != element_id]
        connection.write_file(updated_answers, 'ask-mate-python/sample_data/answer.csv')


def sorting_questions(type_of_filter, value):
    questions = get_questions()
    if type_of_filter == "by_date":
        filtered_questions = sorted(questions, key=lambda i: i['submission_time'], reverse=value)
    else:
        filtered_questions = sorted(questions, key=lambda i: i['vote_number'], reverse=value)
    return filtered_questions


def sprawdzajko(type):
    questions = get_questions()
    if type == 'submission_time':
        if questions[0][type] < questions[-1][type]:
            value = True;
        else:
            value = False;
    else:
        if int(questions[0][type]) < int(questions[-1][type]):
            value = True;
        else:
            value = False;
    return value


def question_view_count_increase(id):
    questions = connection.import_data('ask-mate-python/sample_data/question.csv')
    for question in questions:
        if question['id'] == id:
            question['view_number'] = str(int(question['view_number']) + 1)
    connection.write_file(questions, 'ask-mate-python/sample_data/question.csv')


def update_image(file_type, filename, id):
    data = connection.import_data(f"ask-mate-python/sample_data/{file_type}.csv")
    for element in data:
        if element['id'] == id:
            element['image'] = 'images/' + filename
    connection.write_file(data, f"ask-mate-python/sample_data/{file_type}.csv")


def update_question(id, title, description, file_type):
    questions = connection.import_data('ask-mate-python/sample_data/question.csv')
    for question in questions:
        if question['id'] == id:
            question['title'] = title
            question['message'] = description
    connection.write_file(questions, f"ask-mate-python/sample_data/{file_type}.csv")