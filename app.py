from flask import Flask, request, render_template
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

@app.route('/questions/<num>')
def homepage():
    """Show the title of the survey, the instructions, and a button to start the survey."""

    return render_template('homepage.html', survey=satisfaction_survey)