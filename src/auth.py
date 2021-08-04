import json
TICKETS_ENDPOINT = ".zendesk.com/api/v2/tickets.json?page[size]=25"
class auth(object):
    def __init__(self):
        self.email = None
        self.token = None
        self.link = None
        self.set_credentials(self.read_credentials())
    # Read credentials from the file, return python dictionary object
    def read_credentials(self):
        credentials = open('credentials.json','r')
        credentials = json.load(credentials)
        return credentials
    #Set object variables
    def set_credentials(self,credentials):
        self.email = credentials["email"]
        self.token = credentials["token"]
        self.link = "https://"+credentials["subdomain"]+TICKETS_ENDPOINT

