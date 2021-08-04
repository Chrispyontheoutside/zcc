import requests

#API endpoint with pagination included
TICKETS_HTTPS_ENDPOINT = ".zendesk.com/api/v2/tickets.json?page[size]=25"
class ticket_request(object):
    def __init__(self):
        self.error = None
        self.status_code = None
    ## Sends a HTTP requests via requests, exits if a connection error is thrown
    def get_http_repsonse(self, link, email, token):
        if(type(link) is str):
            try:
                return requests.get(link, auth = (email+'/token', token),timeout=1)
            except requests.ConnectionError:
                self.error = "Network problem, could not connect (DNS failure, refused connection, etc)"

        else:
            raise ValueError("The endpoint (url) was not a string")
    # Sets status code of the response
    def return_status_code(self,response):
        self.status_code = response.status_code
        if response.status_code == 200:
            return True
        else:
            self.error = response.json()["error"]
    # Returns the next endpoint for the page
    def return_new_endpoint(self,responseJson):
            return responseJson["links"]["next"]
    # Returns true if the has_more key is true in the response
    def check_hasmore(self,responseJson):
        return (responseJson["meta"]["has_more"]==True)
    #Text processing to format date and time
    def convert_time(self,dateTime):
        if type(dateTime) is str:
            try:
                date, time = dateTime.strip('Z').split('T')
                return date + " | " + time
            except:
                self.error = "Ran into issues converting date and time"
        else:
            raise 
    def ticket_time_set(self,responseJson):
        for ticket in responseJson["tickets"]:
            ticket["created_at"] = self.convert_time(ticket["created_at"])
            ticket["updated_at"] = self.convert_time(ticket["updated_at"])
        return responseJson
    #Sets value of tickets
    def retrieve_tickets(self,email,token,link):
        response = self.get_http_repsonse(link,email,token)
        if(self.error == None and self.return_status_code(response)):
            tickets = []
            tickets.append(self.ticket_time_set(response.json()))
            #Check last item in tickets to see if there are still tickets to request
            while(self.check_hasmore(tickets[-1])):
                #response is a new response from the endpoint provided from previous response
                response = self.get_http_repsonse(self.return_new_endpoint(tickets[-1]),email,token)
                if(not self.return_status_code(response)):
                    return self.status_code
                tickets.append(self.ticket_time_set(response.json()))
            return tickets
        else:
            return self.error