import sys
from signal import SIGINT
from os import path, kill, getpid
sys.path.append(path.dirname(path.abspath(__file__)) + '/static/python')
from flask import Flask, render_template, request, jsonify
from static.python import algorithms, midterm

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shutdown', methods=['POST'])
def shutdown():
    kill(getpid(), SIGINT)
    return 'Server shutting down...'

@app.route('/sm-1')
def sm_1():
    return render_template('sm-1.html')


@app.route('/sm-1/<mode>', methods=['POST'])
def code():
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
def code_2(mode: str) -> str:
    header = request.form['header']
    txt = request.form['text']

    military_algorithm_map = {
        'ENCODE': algorithms.Encode_Millitary_Message,
        'DECODE': algorithms.Decode_Millitary_Message,
    }

    if mode.upper() not in military_algorithm_map.keys():
        return "<h3>Invalid mode selected</h3>"

    result: str = military_algorithm_map[mode.upper()](txt, header)
    return f"<h3 style='word-break: break-word;'>{result}</h3>"

@app.route('/units', methods=['GET', 'POST'])
def units():
    if request.method == 'POST':
        category = request.form['category'].lower()
        amount = float(request.form['amount'])
        unit1 = request.form['unit1'].lower()
        unit2 = request.form['unit2'].lower()
        return f'<h3>{midterm.calculate(amount, category, unit1, unit2)}</h3>'
    return render_template('unit-calc.html', categories=list(midterm.units.keys()))

@app.route('/units/api')
def units_api():
    return jsonify(midterm.units)