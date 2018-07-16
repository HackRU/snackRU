# SnackRU

## Description
Goals
a. to keep track of snack consumption rates for future reference
b. to remind volunteers about which things to ration 
c. delegate tasks like getting water for percolator at predetermined times/making coffee/perform extra cleanup to individual volunteers so that directors don't have to constantly remind them


## Inspiration
This app was born out of the desire to use the name "SnackRU"

## Installation Guide

Before starting (for the team)

Languages/Frameworks
- Use Flask to make a python webapp.
- Use mongoDB to store data about snacks and users (probably using mongoengine python library)
- Jinja2 templating is used to display the front end (this is standart with Flask apps)


If you haven’t worked with flask before, read up on the basics of Flask
http://flask.pocoo.org/docs/1.0/quickstart/

From the docs, you should at least know how to…
- use app.route( )
- return redirects to different routes
- render HTML templates & pass in variables
- deal with requests


If you plan on dealing with the database, read the mongoengine docs
	http://docs.mongoengine.org/guide/index.html
	
Know how to…
- connect to a database
- query the db
- define  a “schema” for your db
    

If you plan on working with the frontend, read about Jinja2 syntax
http://jinja.pocoo.org/docs/2.10/templates/

Know how to…
- use for loops and conditionals to display elements
  

If you want to deal with login
https://flask-login.readthedocs.io/en/latest/
- login forms http://flask.pocoo.org/docs/1.0/patterns/wtforms/

Note that all of these components are sort of connected, so it would benefit everyone to read all of the docs at some point. 

## Example Uses

- Volunteers can increment snack counts when hackers take snacks
- directors can post notifications to volunteers if they need something done ASAP
- App will notify users every 30 min to clean table/refill coffee

## Style Guide

PEP8
https://www.python.org/dev/peps/pep-0008/

## TO-DO List

Necessary Features
- A login for volunteers
- A way for volunteers to keep a count of which snacks are taken
      - I don’t really care how this is implemented, but try to make it as convenient as possible for volunteers
- A way to remind volunteers what snacks should be placed out at what times
      - In previous years, we had physical spreadsheets
- A “alert” box that reminds volunteers to do things at specific time intervals


## Links to Further docs
n/a

## And whatever you want :tada:
nothing
