from flask import Flask, render_template, request
import data_manager


app = Flask(__name__)


@app.route('/')
def main_page():
    question = request.form
    return render_template("index.html")


@app.route('/list')
def list_of_questions():
    return render_template("list.html")


@app.route('/add', methods=['GET', 'POST'])
def add_question():
    question = request.form
    return render_template("add.html")


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run()