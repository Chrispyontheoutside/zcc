import ticket_request
class tickets(object):
    def get_individual_ticket(self,ticket_id):
        if(type(self.tickets) == list):
            try:
                ticket_id = int(ticket_id)
            except Exception:
                raise ValueError
            ##Because a ticket_id does not start at 0, and the ticket list is a list of the requests or total number of tickets // 25 
            if(ticket_id%25 == 0):
                ticket_array_index = (ticket_id//25)-1
            else:
                ticket_array_index = ticket_id//25
            try:
                return self.tickets[ticket_array_index]["tickets"][(ticket_id%25)-1]
            except:
                raise IndexError("The provided ticket number is out of bounds")
        else:
            raise ValueError
    ## Returns total number of tickets by checking the id of the last ticket
    def total_tickets(self):
        total_num_tickets=0
        for paginatedItem in range(len(self.tickets)):
            total_num_tickets += len(self.tickets[paginatedItem]["tickets"])
        return total_num_tickets
    def create_tickets(self,email,token,subdomain):
        self.ticket_request = ticket_request.ticket_request()
        self.tickets = self.ticket_request.retrieve_tickets(email,token,subdomain)
        self.status_code = self.ticket_request.status_code
        self.error = self.ticket_request.error
