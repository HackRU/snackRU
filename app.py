from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"

#Route for handling login
@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    return "login page!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)


