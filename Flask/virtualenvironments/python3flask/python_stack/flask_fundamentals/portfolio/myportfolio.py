from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def portfolio():
	return 'Welcome to my portfolio! My name is Blaine'
@app.route('/projects')
def projects():
	print ("My Projects")
	print ("-portfolio")
	print ("-meowmix")
	print ("-study on sleep")
	return ("-quest for unicorns")
@app.route('/about')
def about():
	return "My name is Blaine. I am from Ukraine. They call me insane. I'm anything but plain. You will remember my name."
app.run(debug=True)