# virtual environment
# 	why use it
# 	how to setup
# flask overview
# 	what is a web framework
# 	advantages/disadvantages
# flask installation
# # 	from import_flash
# http req/res cycle
# 	enter espnt.com
# 	send get request
from flask import flask, render_template
import random

app = flask(__name__)

app.run()

@app.route('/')
def apple():
	return render_template('index.html',\
		numone = random.random(0,100),\
		names = ['jim'])
@app.route('/nba')
def nba():
	return("you visited the nba page")
app.run(debug=True)as