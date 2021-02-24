""" Views (functions) for various pages

DEV: Jordan Landgrebe
2021-02-23
"""


def homepage():
    return '''
<html>
    <head>
        <title>Ikon Reservation Notification System</title>
    </head>
    <body>
        <h1>Welcome to the Ikon Pass Reservation Notification System!</h1>
        <p>Select on of the available mountains to configure notifications</p>
    </body>
</html>'''


def say_hello_test():
    from http_requests.make_request import Requester
    from table_makers.copper_mountain_table import Table

    from config.splash_config import SPLASH_CONFIG
    from config.site_config import COPPER_MOUNTAIN

    # Get the raw response result
    requester = Requester(SPLASH_CONFIG, COPPER_MOUNTAIN)
    response = requester.get_response()

    # Create table
    table = Table(response)
    from pandas import DataFrame
    table = DataFrame(table._events)
    return '<p>' + table.to_string() + '</p>'
