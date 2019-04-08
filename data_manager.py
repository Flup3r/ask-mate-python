import connection


def get_all_answers():
    a_list = connection.import_question('answers.csv')
    return a_list
