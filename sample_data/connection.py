import csv


def import_question(filename):  # import csv data
    with open(filename, "r") as file:
        imported_data = csv.DictReader(file)
        data = list(imported_data)
        return data


def write_file(dict_list, filename="questions.csv"):
    keys = ["id", "submission_time", "view_number", "vote_number", "title", "message", "image"]
    if filename == 'answers.csv':
        keys = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']
    file_directory = 'data/' + filename
    with open(file_directory, 'w') as f:
        writer = csv.DictWriter(f, keys)
        writer.writeheader()
        writer.writerows(dict_list)
