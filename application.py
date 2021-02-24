""" Flask interface for Project

DEV: Jordan Landgrebe
2021-02-23
"""
from flask import Flask
import sqlite3

# Create Application Object
application = Flask(__name__)

# Setup DB Definitions
conn = sqlite3.connect('databases.db')
conn.execute('CREATE TABLE users (email TEXT)')


# Add a URL Rule for the homepage
from flask_app.views import homepage
application.add_url_rule('/', 'index', lambda: homepage())


if __name__ == '__main__':
    application.debug = True
    application.run()
