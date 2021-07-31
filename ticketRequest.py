import requests
import sys
TICKETS_HTTPS_ENDPOINT = ".zendesk.com/api/v2/tickets.json?page[size]=25"
class ticketrequest(object):
    def __init__(self,email = "chrispeterfrancis@tamu.edu" ,pw = "Trickster.Cleaver.Negative5",domain = 'zcctamuchris'):
        self.email = email
        self.pw = pw
        self.link = "https://"+domain+".zendesk.com/api/v2/tickets.json?page[size]=25"
        self.status_code = None
        self.response_text = None
        self.tickets = self.returnTickets()
    ## Sends a HTTP requests via requests, exits if a connection error is thrown
    def getHTTPResponse(self, endpoint):
        try:
            return requests.get(endpoint, auth = (self.email,self.pw))
        except requests.ConnectionError:
            print("Network problem, could not connect (DNS failure, refused connection, etc)")
            sys.exit()
    ## Sets status code of the response
    def returnStatusCode(self,response):
        self.status_code = response.status_code
        if response.status_code == 200:
            return True
        else:
            self.response_text = response.json()["error"]
    def returnRepsonseJson(self,response):
            try:
                return response.json()
            except:
                print("Could not return json")
    ## Returns the next endpoint for the page
    def returnNewEndpoint(self,responseJson):
            return responseJson["links"]["next"]
    ## Returns true if the has_more key is true in the response
    def checkHasMore(self,responseJson):
        return (responseJson["meta"]["has_more"]==True)
    #Sets value of tickets
    def returnTickets(self):
        response = self.getHTTPResponse(self.link)
        if(self.returnStatusCode(response)):
            tickets = []
            tickets.append(self.returnRepsonseJson(response))
            while(self.checkHasMore(tickets[-1])):
                response = self.getHTTPResponse(self.returnNewEndpoint(tickets[-1]))
                if(not self.returnStatusCode(response)):
                    return None
                tickets.append(self.returnRepsonseJson(response))
            return tickets
        else:
            return None
    ##Get a particular ticket from the list of tickets
    def getTicket(self,ticketID):
        ##Because a ticketID does not start at 0, and the ticket list is a list of the requests or total number of tickets // 25 
        if(ticketID%25 == 0):
            ticketArrayIndex = (ticketID//25)-1
        else:
            ticketArrayIndex = ticketID//25
        return self.tickets[ticketArrayIndex]["tickets"][(ticketID%25)-1]
    ## Returns total number of tickets by checking the id of the last ticket
    def totalTickets(self):
        return self.tickets[-1]["tickets"][-1]["id"]
