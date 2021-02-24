""" Objects related to making the requests to websites

DEV: Jordan Landgrebe
2021-02-19
"""
import requests


class Requester(object):

    def __init__(self, splash_config, site_config, **kwargs):
        """ Create a request object """
        self._splash_config = splash_config
        self._site_config = site_config
        self._response = None

    def _store_response(self, response):
        self._response = response

    def get_response(self, new=False):
        """ Using class attributes, get and store the HTTP Response Object """
        if self._response is None:
            r = requests.get(self._splash_config['url'], params=self._site_config)
            self._store_response(r)
        return self._response

