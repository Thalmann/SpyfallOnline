from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask_wtf import Form
from wtforms.fields import SubmitField, StringField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

class StartGameForm(Form):
    """Simple form when creating a new game."""
    
    text = StringField('Name:')
    submit = SubmitField('Start Game')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/games')
def games():
    return render_template('games.html')

@app.route('/new_game', methods=['GET', 'POST'])
def new_game():
    form = StartGameForm()
    if form.validate_on_submit():
        if form.text.data != '':
            return render_template('game.html', game_name = form.text.data)
    return render_template('new_game.html', form = form)

@app.route('/game')
def game():
    return render_template('game.html')

if __name__ == '__main__':
    app.run(debug = True)
