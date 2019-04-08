from flask import Flask, render_template, request
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

@app.route('/show_question')       #transfers id from list of questions
def show_question():
    return render_template("show_question.html")

@app.route('/add', methods=['GET', 'POST'])
def add_question():
    question = request.form
    return render_template("add.html")

@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run()