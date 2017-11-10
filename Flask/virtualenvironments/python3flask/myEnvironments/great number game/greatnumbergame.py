from flask import Flask, render_template, session, redirect, flash
import random

app = Flask(__name__)
app.secret_key = "keepitsecret"

@app.route('/')
def index():
    if not 'num' in session:
        session['num'] = random.randrange(0,101)
        return render_template('index.html')

@app.route('/guess')
def guess():
    if 'num' > 'guess':
        sesssion.pop('guess')
        print ("Too low!")
        print ("Guess again")
        return redirect('/')
    if 'num' < 'guess':
        session.pop('guess')
        print ("Too high!")
        print ("Guess again")
        return redirect('/')
    else:
        return redirect('/reset')
#
# @app.route('/higher'):
# def higher():
#     session['']
#
# @app.route('/lower')
# def lower():
#     session['']

@app.route('/reset', methods=['POST'])
def reset():
    print ("You guessed my number!")
    session.pop('num')
    return redirect('index.html')

app.run(debug=True)
