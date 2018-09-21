from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

#Route for handling login
@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    return "THis is a login page!!!!!"
