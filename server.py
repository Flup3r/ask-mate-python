from datetime import datetime

from flask import Flask, render_template, request

import connection
import data_manager

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
    return render_template("show_question.html")




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
    new_question = {
        'id': new_id,
        'submission_time': data,
        'view_number': 0,
        'vote_number': 0,
        'title': 'title',
        'message': "message",
        'image': "none"
    }
    new_data = data_manager.get_questions()
    new_data.append(new_question)
    connection.write_file(new_data, 'question.csv')
    return render_template("add.html")




if __name__ == '__main__':
    app.run()