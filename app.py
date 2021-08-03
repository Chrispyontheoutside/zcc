import auth
import tickets
from flask import Flask, render_template, request
from flask_paginate import Pagination, get_page_parameter

app = Flask(__name__)
tickets_list = None
@app.route('/')
def serve_app():
    if(tickets_list.error == None):
        page = request.args.get(get_page_parameter(), type=int, default=1)
        pagination = Pagination(page=page, total=tickets_list.total_tickets(), record_name='tickets', css_framework='bulma', per_page = 25)
        page_request = request.args.get("page")
        if(page_request == None):
            page_request = 0
        else:
            page_request = int(page_request)-1
        return render_template('index.html', tickets=tickets_list.tickets[page_request]["tickets"], pagination = pagination)
    else:
        return render_template('error.html',response = tickets_list.error)

@app.route('/ticket/<int:id>')
def serve_ticket(id):
    individual_ticket = tickets_list.get_individual_ticket(id)
    return render_template('ticket.html',ticket = individual_ticket, url=request.referrer,tags = individual_ticket["tags"])

#Create object with credentials (email, token, subdomain)
auth = auth.auth()
tickets_list = tickets.tickets()
tickets_list.create_tickets(auth.email,auth.token,auth.subdomain)
app.run(debug=True)