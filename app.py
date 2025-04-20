import sys
from os import path
sys.path.append(path.dirname(path.abspath(__file__)) + '/static/python')
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length
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

@app.route('/sm-2')
def sm_2():
    return render_template('sm-2.html')

@app.route('/sm-2/<mode>', methods=['POST'])
def code_2(mode):
    header = request.form['header']
    txt = request.form['text']

    military_algorithm_map = {
        'ENCODE': algorithms.Encode_Millitary_Message,
        'DECODE': algorithms.Decode_Millitary_Message,
    }

    if mode.upper() not in military_algorithm_map.keys():
        return "<h3>Invalid mode selected</h3>"

    result = military_algorithm_map[mode.upper()](txt, header)
    return f"<h3 style='word-break: break-word;'>{result}</h3>"

