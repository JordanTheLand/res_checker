""" Flask interface for Project

DEV: Jordan Landgrebe
2021-02-23
"""
from flask import Flask


def say_hello():
    return "<p>Hello Jordan</p>"


# Create Application Object
application = Flask(__name__)


# Add a URL Rule for the homepage
application.add_url_rule('/', 'index', lambda: say_hello())

if __name__ == '__main__':
    application.debug = True
    application.run()
