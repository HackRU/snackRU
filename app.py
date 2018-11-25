import os
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template, redirect, url_for, flash
import csv
import xlrd
from mongoengine import connect
from passlib.hash import sha256_crypt

#from user-defined files
from mongo import DbUser, DbFood
from forms import loginForm

app = Flask(__name__)
app.secret_key = "super_secret"

#INIT THE DATABASE
connect("snackRU")


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
    form = loginForm()
    return render_template('login.html', form=form)


@app.route('/login', methods=['POST'])
def login():
    error = None
    username = request.form["user"]
    password = request.form["password"]
    # TODO:authenticate

    #check if password is good
    print("form validated")
    storedPw = DbUser.objects(username=username).first().password 
    
    #verify will break if the password is not a sha_256 hash
    #which is to say, if you try to login as a user created before hashing was implemented
    if(sha256_crypt.verify(password, storedPw)):
        return redirect('/food')
    else:
        return redirect('login')

    return redirect('login')


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

    #TODO: parse through excel file and insert into database
    workbook = xlrd.open_workbook('xcel/Snack-Table-Guide.xlsx')
    worksheet = workbook.sheet_by_index(0)
    #In the sheet, firstCol:Category, secCol:foodname, thirdCol:quant
    #Can we start the list from row 11?
    row = 10
    while sheet.cell(row,1).value != xlrd.empty_cell.value:
        foodname = sheet.cell(row,1).value
        foodquant = sheet.cell(row,2).value
        foodcat = sheet.cell(row,0).value
        #are we creating a food object?
        dbfood = DbFood(foodName = foodname, quantity = foodquant, category = foodcat).save()
        row += 1
    

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

    #make sure user email is unique
    if DbUser.objects(username=username):
        print("error: user already exists")
        return redirect('/register')
    
    #hash the password
    hashPw = sha256_crypt.encrypt(password)
    

    #save user to database
    dbUser = DbUser(username = username, password = hashPw, email=email).save()
    
    return redirect('/login')  # should I use url_for? maybe if url changes
    # return render_template('register.html', form=form) #redirect if neccesary

def allowed_file(fname):
    return '.' in fname and fname.rsplit('.',1)[1].lower() == "xlsx"

@app.route('/upload', methods=['POST'])
def upload_post():
    #upload failed
    print(request)
    if 'file' not in request.files:
        print("err1")
        flash('Upload failed, try again')
        return redirect('/upload')
    
    file_ = request.files['file']
    if file_.filename == '':
        print("err2")
        flash('No file selected :/')
        return redirect('/upload')

    if file_ and allowed_file(file_.filename):
        print("err3")
        filename = secure_filename(file_.filename)
        file_.save(os.path.join("/home/ubuntu/Workspace/snackRU/xcel/", filename))
        flash('Upload successful!')
        return redirect('/current_food')
    else:
        print("err4")
        flash('Bad file type')
        return redirect('/upload')
    

@app.route('/upload', methods=['GET'])
def upload_get():
    return render_template('upload.html')
    

# some error check
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    # port = int(os.environ.get('PORT', 5000))
<<<<<<< HEAD

=======
    app.run(host='0.0.0.0', port=9000, debug=True)
>>>>>>> a0eb156173ed0f1b6ebb579358f97ebe934bfd9a
