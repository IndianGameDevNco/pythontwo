from flask import Flask, render_template, request, url_for
from static.python import algorithms

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sm-1')
def sm_1():
    return render_template('sm-1.html')

@app.route('/sm-1/<mode>', methods=['POST'])
def code(mode):
    algorithm = request.form['algorithm']
    mode = request.form['mode']
    txt = request.form['text']
    return f"<h3 style='word-break: break-word;'>{eval(f"algorithms.{algorithm}(txt)")}</h3>"

