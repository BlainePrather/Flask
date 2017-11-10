from flask import Flask, render_template, session, redirect
app = Flask(__name__)

app.secret_key = 'mypumalife'

@app.route('/')
def index():
    if not 'num' in session:
        session['num'] = 0
    session['num'] += 1
    return render_template('index.html')

@app.route('/num', methods=['POST'])
def number():
    session['num'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def resetnum():
    session['num'] = 0
    return redirect('/')
app.run(debug=True)
