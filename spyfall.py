from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/games')
def games():
    return render_template('games.html')

@app.route('/new_game.html')
def new_game():
    return render_template('new_game.html')

if __name__ == '__main__':
    app.run(debug = True)
