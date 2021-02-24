""" Run script for Copper Mountain """
from http_requests.make_request import Requester
from table_makers.copper_mountain_table import Table

from config.splash_config import SPLASH_CONFIG
from config.site_config import COPPER_MOUNTAIN

# Get the raw response result
requester = Requester(SPLASH_CONFIG, COPPER_MOUNTAIN)
response = requester.get_response()

# Create table
table = Table(response)






