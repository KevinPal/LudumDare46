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
    blank = [[("#f00", "#fff", "&nbsp") for _ in range(80)] for _ in range(25)]
    screens = []

    for i in range(10):
        frame = copy.deepcopy(blank)
        frame[i    ][i    ] = ("#000", "#fff", "&nbsp")
        frame[i    ][i + 1] = ("#000", "#fff", "&nbsp")
        frame[i + 1][i    ] = ("#000", "#fff", "&nbsp")
        frame[i + 1][i + 1] = ("#000", "#fff", "&nbsp")
        screens.append(frame)
    return render_template('screens.jinja', screens=screens)
