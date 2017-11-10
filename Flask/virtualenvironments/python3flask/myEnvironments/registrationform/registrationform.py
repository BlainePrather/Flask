from flask import Flask, render_template, redirect, flash, session
import re
app = Flask(__name__)
app.secret_key = "keepitsecret"
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+')
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
	if len(request.form['email']) < 1 or len(request.form['firstname']) < 1 or len(request.form['lastname']) <1 or len(request.form['password']) < 1 or len(request.form['confirmpassword']):
		flash("All fields are required and must not be blank")
		error = True
	if not request.form['firstname'].isalpha() or not request.form['lastname'].isalpha():
		flash("first and last name cannot contain any numbers")
		error = True
	if len(request.form['password']) <= 8:
		flash("password must be longer than 8 characters")
		error = True
	if email_regex.match(request.form['email']):
		flash("Email should be a valid email")
		error = True
	if error:
		return ('')
	else:
		session['email'] = request.form['email']
		session['firstname'] = request.form['firstname']
		return redirect('/success')

@app.route('/success')
def success():
	return "You're Registered"
app.run(debug=True)
