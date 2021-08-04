# Zendesk Coding Challenge by Chris Peter Francis

## Description
This is my attempt at the Zendesk Coding Challenge for the Cloud Engineering Co-Op Role. In the challenge, participants were asked to build a application (GUI or CLI) to serve tickets from the Zendesk Ticket API using any technology stack. 

## Objectives
- Retrieve Tickets from the Zendesk Ticket API
- Request all the tickets from the account
- Display them in a list 
- Display individual ticket details
- Paginate if ticket count > 25

## Preview 
- Ticket Viewer
![Imgur](https://i.imgur.com/JoIgcXk.png)
- Single Ticket View
![Imgur](https://i.imgur.com/Vk2NZkI.png)
- Error Page
![Imgur](https://i.imgur.com/bBUPcdN.png)

## Installation Prerequisites
- [python 3.8.2, pip 19.2.3]
- `pip install -r requirements.txt`

## Authentication
- In the credentials.json file in src/, update the email, token and subdomain to the appropriate data.

## Running 
- versions: `python src/app.py`
- `http://127.0.0.1:5000` in your prefered browser :)

## Testing
- Created unit tests using Python's unittest module | implementing more coverage with respect to not sending requests with tests
- `python -m unittest src/`

## Improvements with Time / Tasks
- Work on effeciency and refactor code
- Write Flask tests | Selenium Web Automation tests
- Edge cases for testing
- Live demo

### Tools Used
- Zendesk Ticket API
- Python
    - Flask
        - flask_paginate
    - requests
    - unittest
- Bulma
  
