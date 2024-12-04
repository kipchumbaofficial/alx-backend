#!/usr/bin/env python3
""" Flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ Configuration Class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Gets the best matching locale from request
    """
    locale = request.args.get('locale')
    if locale:
        if locale in app.config['LANGUAGES']:
            return locale
    return request.accept_languages.best_match(
            app.config['LANGUAGES'])


@app.route('/')
def index():
    """ Renders index.html
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run()