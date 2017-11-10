from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/ninjas')
def ninjas():
    print ("ninjas page")
    return render_template('ninjas.html')
# @app.route('/dojos')

app.run(debug=True)
