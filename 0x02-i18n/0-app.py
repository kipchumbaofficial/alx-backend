#!/usr/bin/env python3
""" Flask app
"""
from flask import Flask, render_template


app = Flask()


@app.route('/')
def index():
    """ Renders index.html
    """
    return render_template('index.html')
