from flask import Blueprint, render_template, url_for, jsonify, redirect, session, request
from ..data.typechart import typechart
import random

pokemon_bp = Blueprint("pokemon_bp", __name__)


@pokemon_bp.route('/')
def home():
    return render_template('/pokemon/pokemon.html')


@pokemon_bp.route('/typechart-quiz', methods=['GET', 'POST'])
def quiz_typechart():

    TOTAL_QUESTIONS = 5

    if 'questions' not in session:
        # If 'questions' key doesn't exist in the session, initiate a new quiz session.
        session['questions'] = random.sample(typechart, TOTAL_QUESTIONS)
        session['current_question'] = 0
        session['score'] = 0

    if request.method == "POST":
        user_answer = request.form.get('effectiveness')
        correct_answer = session['questions'][session['current_question']]['correct_answer']

        # Keep track of user's answer
        session['questions'][session['current_question']]['user_answer'] = user_answer

        if user_answer == correct_answer:
            session['score'] += 1

        session['current_question'] += 1

    if session['current_question'] < TOTAL_QUESTIONS:
        current_question = session['questions'][session['current_question']]
        return render_template('/pokemon/quiz_typechart.html',
                               current_question_number=session['current_question'] + 1, current_question=current_question,
                               total_questions=TOTAL_QUESTIONS)
    else:
        return redirect(url_for("pokemon_bp.quiz_result"))


@pokemon_bp.route('/result')
def quiz_result():
    questions = session['questions']
    score = session['score']
    return render_template('/pokemon/result.html', questions=questions, score=score)


@pokemon_bp.route('/reset', methods=['POST'])
def quiz_reset():
    session.pop('questions', None)
    session.pop('current_question', None)
    session.pop('score', None)
    return redirect(url_for('pokemon_bp.quiz_typechart'))
