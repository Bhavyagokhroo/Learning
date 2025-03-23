## building url dynamically
## variable rule 
## jinja 2 tempelate engine 
'''
multiple ways 
1) '{{}}' expressions to build output in html 
2) '{%...%}' conditions,for loops
3) '{#...#}' this is used for comments
'''
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

@app.route('/submit',methods = ['GET','POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name}!"
    return render_template('form.html')
# #vriable rule
# @app.route('/success/<int:score>')
# def success(score):
#     return f"The marks you got is {score}"

@app.route('/success/<int:score>')
def success(score):
    res = ''
    if score >= 50:
        res = "PASS"
    else:
        res = "FAIL"

    return render_template('result.html',results = res)

@app.route('/successres/<int:score>')
def successres(score):
    res = ''
    if score >= 50:
        res = "PASS"
    else:
        res = "FAIL"

    exp = {'score':score,"res":res}

    return render_template('result1.html',results = exp)

@app.route('/successif/<int:score>')
def successif(score):
    res = ''
    

    return render_template('result2.html',results = score)

@app.route('/fail/<int:score>')
def success(score):
    

    return render_template('result.html',results = score)


if __name__ == "__main__": #entry point of any py file
    app.run(debug=True) # this will run the app
    # debug = True means whenever we will press ctrl + s changes will be made to website

# we can use return redirect(url_for()) to redirect to any page we want 



