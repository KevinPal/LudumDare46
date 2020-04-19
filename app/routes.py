from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html.jinja')

bg_char = "<span style='background-color: #f00'>&nbsp</span>"
black = "<span style='background-color: #000'>&nbsp</span>"

import textwrap
import copy
@app.route("/test_animation")
def test_animation():
    blank = [[bg_char for _ in range(80)] for _ in range(25)]
    screens = []

    for i in range(10):
        frame = copy.deepcopy(blank)
        frame[i    ][i    ] = black
        frame[i    ][i + 1] = black
        frame[i + 1][i    ] = black
        frame[i + 1][i + 1] = black
        screens.append("\n".join(["".join(line) for line in frame]))
    return "\n".join(screens)
