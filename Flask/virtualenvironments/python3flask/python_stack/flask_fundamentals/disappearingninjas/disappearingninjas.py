from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
@app.route('/ninja')
def allninjas():
	return render_template('ninjas.html')
@app.route('/ninja/<color>')
def single_ninja(color):
	if color == "blue":
		color_str = "leonardo.jpg"
	elif color = "orange":
		color_str = "michelangelo.jpg"
	elif color = "red":
		color_str = "rafael.jpeg"
	elif color = "purple":
		color_str = "donatello"
	else:
		color_str ="notapril.jpg"	
	return (redirect('/', color_string = color_str))
app.run(debug=True)