from flask import Flask

app = Flask(__name__)  # It creates an interface of Flask class which will be our wsgi application

@app.route("/")  # "/" means it will become the home page
def welcome():
    return "Welcome to flask course" #whenever we will have only "/" then this function will execute and this will be printed
@app.route("/index")
def welcome1():
    return "Welcome to the index page"

if __name__ == "__main__": #entry point of any py file
    app.run(debug=True) # this will run the app
    # debug = True means whenever we will press ctrl + s changes will be made to website
