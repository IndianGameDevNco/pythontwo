from flask import Flask, render_template, request
from os import path
import sys
sys.path.append(path.dirname(path.abspath(__file__)) + '/static/python')
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
    txt = request.form['text']
    algorithm_map = {
        'Odd_Even_Swap': algorithms.Odd_Even_Swap,
        'Reverse': algorithms.Reverse,
        'Reverse_Word': algorithms.Reverse_Words,
        'Half_Swap': algorithms.Half_Swap,
        'Bit_Flip': algorithms.Bit_Flip
    }
    if algorithm not in algorithm_map:
        return "<h3>Invalid algorithm selected</h3>"
    result = algorithm_map[algorithm](txt)
    return f"<h3 style='word-break: break-word;'>{result}</h3>"

