from mongoengine import *

class DbUser(Document):
    username = StringField(max_length=10, required=True)
    password = StringField(required=True) #this will be hashed
    email = EmailField(required=True) #idk how this works tho

class DbFood(Document):
    foodName = StringField(required = True)
    quantity = StringField()
    category = StringField()

