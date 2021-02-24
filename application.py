""" Flask interface for Project

DEV: Jordan Landgrebe
2021-02-23
"""
from flask import Flask

# Create Application Object
application = Flask(__name__)

# Add a URL Rule for the homepage
from flask_app.views import say_hello_test
application.add_url_rule('/', 'index', lambda: say_hello_test())


if __name__ == '__main__':
    application.debug = True
    application.run()
