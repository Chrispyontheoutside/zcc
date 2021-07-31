from flask import Flask, render_template, request
import ticketRequest
from flask_paginate import Pagination, get_page_parameter

app = Flask(__name__)
tickets = []

@app.route('/')
def serve_app():
    if(tickets.status_code == 200):
        page = request.args.get(get_page_parameter(), type=int, default=1)
        pagination = Pagination(page=page, total=tickets.totalTickets(), record_name='tickets', css_framework='bulma', per_page = 25)
        page_request = request.args.get("page")
        if(page_request == None):
            page_request = 0
        else:
            page_request = int(page_request)-1
        return render_template('index.html', tickets=tickets.tickets[page_request]["tickets"], pagination = pagination)
    else:
        print(tickets.response_text, tickets.status_code)
        return render_template('error.html',response = tickets.response_text)
@app.route('/ticket/<int:id>')
def serve_ticket(id):
    individual_ticket = tickets.getTicket(id)
    return render_template('ticket.html',ticket = individual_ticket, url=request.referrer,tags = individual_ticket["tags"])

    

if(__name__ == "__main__"):
    tickets = ticketRequest.ticketrequest()
    app.run(debug=True)
    