#!/usr/bin/env python3
'''Basic Flask app'''
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    '''Config class'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)

app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    '''Gets locale'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    '''Index route'''
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
