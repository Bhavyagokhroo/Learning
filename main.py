from flask import Flask,render_template #this render_template will

app = Flask(__name__)  # It creates an interface of Flask class which will be our wsgi application

@app.route("/")  # "/" means it will become the home page
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>" #but this is not a good practise to write whole html code here
@app.route("/index")
def welcome1():
    return render_template('index.html')

if __name__ == "__main__": #entry point of any py file
    app.run(debug=True) # this will run the app
    # debug = True means whenever we will press ctrl + s changes will be made to website
