from datetime import datetime

import connection
import data_manager
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def main_page():
    question = request.form
    return render_template("index.html")


@app.route('/list')
def list_of_questions():
    questions = data_manager.get_questions()
    return render_template('list.html', questions=questions)


@app.route('/show_question/<id>')       #transfers id from list of questions
def show_question(id):
    question = data_manager.one_question(id)
    answers = data_manager.get_answers_to_question(id)
    return render_template("show_question.html", question=question, answers=answers)


@app.route('/question/<id>/new-answer', methods=['GET', 'POST'])
def route_new_answer(id):
    if request.method == 'POST':
        data_manager.add_answer(request.form, id)
        return redirect('/show_question/' + id)
    return render_template('answer.html', id=id)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/add-question', methods=['GET', 'POST'])
def add_question():
    question = request.form
    return render_template("add.html")


@app.route('/add', methods=['GET', 'POST'])
def add():
    data = datetime.now()
    data = str(data)

    last_id = data_manager.get_questions()
    last_id = last_id[-1]['id']
    if int(last_id) > -1:
        new_id = int(last_id) + 1
    else:
        new_id = 0
    if request.method == 'POST':
        new_question = {
        'id': new_id,
        'submission_time': data,
        'view_number': 0,
        'vote_number': 0,
            'title': request.form['title'],
            'message': request.form["message"],
            'image': None
        }
    else:
        return render_template('add.html')
    new_data = data_manager.get_questions()
    new_data.append(new_question)
    connection.write_file(new_data, 'ask-mate-python/sample_data/question.csv')
    print('NoError')
    return redirect('/list')


if __name__ == '__main__':
    app.debug = True
    app.run()