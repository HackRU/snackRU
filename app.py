import os

from flask import Flask, request, render_template, redirect, url_for
import csv
from mongoengine import *


app = Flask(__name__)


class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


class Food():
    def __init__(self, name, id, quantity):
        self.name = name
        self.id = id  # probably barcode id
        self.quantity = quantity

    def enterAmount(self, curr_amnt):  # user enters in current amount
        self.quantity = curr_amnt

    def decrease_quantity(self, decr_amnt):  # user enters how much food that has been used
        self.quantity = self.quantity - decr_amnt

    def increase_quantity(self, incr_amnt):  # user enters how much food that has been gained
        self.quantity = self.quantity + incr_amnt


# FLASK PART
@app.route('/')
def welcome():
    return render_template('snack.html')


@app.route('/', methods=['GET','POST'])
def my_form_post():
    # redirects user
    if request.method == 'POST':
        if request.form['log'] == "login":
            return redirect('/login')
        elif request.form['log'] == "register":
            return redirect('/register')
    else:
        return render_template('snack.html')


@app.route('/login')
def login_welcome():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    error = None
    username = request.form["Username"]
    password = request.form["Password"]
    # TODO:authenticate
    if request.method == 'POST':
        if username != 'admin' or password != 'admin':
            error = 'Invalid credentials! Please try again.'
        else:
            return redirect(url_for('food_welcome'))
    return render_template('login.html')


@app.route('/food')  # TODO: close off to non signed in users - How?
def food_welcome():
    return render_template('food.html')


@app.route('/food', methods=['POST'])
def food():
    # redirects user to site based on if they want to enter or see the food
    if request.method == 'POST':
        if request.form['food'] == "Enter in Food":
            return redirect('/enter_food')
        elif request.form['food'] == "See and Edit Current Food":
            return redirect('/current_food')
    return


# allows user to enter food
@app.route('/enter_food')
def enter_food_welcome():
    return render_template('enter_food.html')


@app.route('/enter_food', methods=['POST'])
# enters in food through file
def enter_food():

    fp = request.files['file']
    if not fp:
        return "No File"

    #TODO: parse through csv file and insert into database


@app.route('/current_food')
def current_food_welcome():
    return render_template('current_food.html')


@app.route('/current_food', methods=['POST'])
def current_food():

    #TODO: show table of food and allow user to edit
    return

@app.route('/register')
def register_welcome():
    return render_template('register.html')


@app.route('/register', methods=['POST'])  # 'GET'?
def register():
    username = request.form["Username"]
    email = request.form["Email Address"]
    password = request.form["New Password"]

    user = User(username, email, password)

    # TODO: save user to database

    return redirect('/login')  # should I use url_for? maybe if url changes
    # return render_template('register.html', form=form) #redirect if neccesary


# some error check
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    # port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=8080, debug=True)
