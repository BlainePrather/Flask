from flask import flask, session, render_template, redirect, request
app = Flash(__name__)

app.secret_key = 'mypumalife'

@app.route('/')
def index(''):
	if 'user' in session:
		status = 'logged in'
	else:
		status = 'not logged in'
	return render_template('index.html', user_name = name, user_email = email)

@app.route('/login', methods = ['POST'])
def login():

	session['name'] = request.form['name']
	session['email'] = request.form['email']
	return redirect('/')

@app.route('/logout')
def logout():
	session.pop('user')
	session.pop('email')
	return restrict('/')

app.run(debug=True)