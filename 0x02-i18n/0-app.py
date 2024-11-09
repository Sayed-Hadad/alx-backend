#!/usr/bin/env python3

"""
This module provides a simple Hello World output.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('0index.html')


if __name__ == '__main__':
    app.run(debug=True)
