import os

from flask import Flask, request, render_template, redirect, url_for
from mongoengine import *
from wtforms import Form, BooleanField, StringField, PasswordField, validators

app = Flask(__name__)


class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password;


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


@app.route('/', methods=['POST'])
def my_form_post():
    text1 = request.form["text1"]
    text2 = request.form["text2"]
    processed_text = text1.upper() + " " + text2.upper()
    return processed_text


@app.route('/login')
def login_welcome():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form["Username"]
    password = request.form["Password"]
    #TODO:authenticate
    authenticated: bool = True
    if authenticated:
        redirect('/food')
    else:
        redirect('/login')


@app.route('/food') #TODO: close off to non signed in users - How?
def food_welcome():
    return render_template('food.html') #TODO: finish food.html


@app.route('/food', methods=['POST'])
def create_food():
    #TODO: somehow create food from spreadsheet/file and then populate database
    return 'filler'


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
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
