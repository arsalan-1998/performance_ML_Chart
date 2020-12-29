from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def singleGraph():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/compare')
def compareGraph():
    if request.method == 'GET':
        return render_template('compare.html')