import unittest
import ticket_request
import json
import auth

class Test_ticket_request(unittest.TestCase):
    def setUp(self):
        self.ticket_request = ticket_request.ticket_request()
        self.test_response_json_data_formatted = (open("test.json",'r'))
        self.auth = auth.auth()
        self.endpoint = self.auth.link
        self.token = "R2ZMun4zoEzd40p9dwbZDUtKvADrCXQzeBXlrP2n"

    def test_convert_time(self):
        self.ticket_request.convert_time("2021-07-27T22:44:11Z")
        self.ticket_request.convert_time("2021-09-27T22:30:11Z")
        self.ticket_request.convert_time("2021-03-27T22:45:11Z")
    