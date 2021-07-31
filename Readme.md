# Zendesk Coding Challenge by Chris Peter Francis

## Description
This is my attempt at the Zendesk Coding Challenge for the Cloud Engineering Co-Op Role. In the challenge, participants were aksed to build a application (GUI or CLI) to serve tickets from the Zendesk Ticket API using any technology stack. 
## Objectives
- Retrieve Tickets from the Zendesk Ticket API
- Display them in a list (Paginate if ticket count > 25)


## Preview 
- Ticket Viewer
![Imgur](https://i.imgur.com/UdAb3VZ.png)
- Single Ticket View
![Imgur](https://i.imgur.com/ovfb1P6.png)

## Live Demo
- Application is running on an EC2 Instance.

## Assumptions
- User knows how to use Docker or is able to install python packages.
- User provides login information and company domain via Docker secrets or Environment Variables.
## Installation
- I have containerized the application to avoid having to install python packages.
- If you would like to run the un-containerized application, I have included the requirements.txt for pip.


## Improvements with Time / Tasks
- Use Token-based authentication to take a least-privelege route.
- Work on effeciency.

### Tools Used
- Zendesk Ticket API
- Python
    - Flask
        - flask_paginate
    - requests
    - unittest
- Bulma
- Docker
- Github Actions
  
## Conclusion
This was a very fun project to work on, hacking away at writing code quickly, prototyping and using a Kanban board to eat away at the project 😁.