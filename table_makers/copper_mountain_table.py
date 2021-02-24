""" Table maker for Copper Mountain """
from bs4 import BeautifulSoup
from pandas import to_datetime


class Table(object):

    def __init__(self, response, **kwargs):
        """ Create pandas dataframe using html response as input """
        self._raw_response = response
        # Create class objects and run setup
        self._soup = BeautifulSoup(response.text, 'html.parser')
        self._store_event_list()
        self._parse_and_store_events()

    def _store_event_list(self):
        """ Store all events as a list """
        events = self._soup.find_all('div', {'class': 'event-item'})
        self._raw_events = events

    def _parse_and_store_events(self):
        """ Loop through events and parse rows """
        event_rows = []
        for event in self._raw_events:
            row = self._parse_event(event)
            event_rows.append(row)
        self._events = event_rows

    def _parse_event(self, event):
        """ Take raw HTML event and return a row """
        row = ['Copper Mountain']
        # Get Date
        date_elm = eval(event.find_all('script')[0].next_element)['startDate']
        date = to_datetime(date_elm)
        row.append(date)
        # Get Parking Status
        parking_elm = event.find_all('div', {'class': 'event-parking'})
        parking = parking_elm[0].text
        row.append(parking)
        # Get HTML Ref
        import pdb
        pdb.set_trace()
        # return full row
        return row
