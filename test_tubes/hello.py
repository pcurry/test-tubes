#!/usr/bin/env python3

from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<p>Hello, world!</p>'
