from flask import Flask,render_template,request #this render_template will

app = Flask(__name__)  # It creates an interface of Flask class which will be our wsgi application

@app.route("/")  # "/" means it will become the home page
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>" #but this is not a good practise to write whole html code here

@app.route("/index",methods = ['GET'])
def welcome1():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form',methods = ['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name}!"
    return render_template('form.html')

@app.route('/submit',methods = ['GET','POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name}!"
    return render_template('form.html')

if __name__ == "__main__": #entry point of any py file
    app.run(debug=True) # this will run the app
    # debug = True means whenever we will press ctrl + s changes will be made to website



# abhi tak isme kya ho raha hain mein batata hu app = Flask(__name__) isne server banaya app.run ne server chalu kiya aur app.route se 
# server chalu hogaya baaki ka code website ki routing e liye aur mainly web application ke liye

#flow of this 
# 1) user url type karta hain 
# 2) flask web server app.run ke through woh request sunta hain 
# 3) aur fir server routing check karta hain ki kaha jaana hain
# 4) fir uss routing mein jaake jo code hota hain woh execute kar deta hain 