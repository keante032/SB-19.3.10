from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def homepage():
    """Show the title of the survey, the instructions, and a button to start the survey."""

    return render_template('homepage.html', survey=satisfaction_survey)

@app.route('/questions/<int:qid>')
def question(qid):
    """Show a form asking the current question, and listing the choices as radio buttons.
    Answering the question should fire off a POST request to /answer."""

    question = satisfaction_survey.questions[qid]
    
    return render_template('question.html', question=question, question_num=qid)

@app.route('/answer', methods=["POST"])
def answer():
    """POST request--append the user's answer to our responses list, then redirect to next question."""

    response = request.form["answer"]
    responses.append(response)
    
    if (len(responses) == len(satisfaction_survey.questions)):
        return redirect("/complete")

    else:
        return redirect(f"/questions/{len(responses)}")