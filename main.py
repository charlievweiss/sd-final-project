"""
Simple "Hello, World" application using Flask

1. Upon visiting the index page at http://127.0.0.1:5000/, 
	the user will be greeted by a page that says hello, and
	includes an input form that requests their name, age, and
	 favorite SoftDes Ninja.
2. Upon clicking the 'Submit' button, the data from the form 
	will be sent via a POST request to the Flask backend at the 
	route POST /login
3. The Flask backend will handle the request to POST /login and 
	perform some simple validation on the user input - simply check 
	to see if they exist.
4. If all the information is present, the app will render a 'profile' 
	page for the user - presenting their name and age. Regardless of their 
	input for final question, their favorite SoftDes ninja, the app will 
	display Patrick Huston
5. If all the information is not present, the app will render 
	a simple error page, which will include some indication that 
	they didn't include all the required information, in addition 
	to a button that will redirect the user back to the home page.

"""

from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login',methods=['POST'])
def login():
	name=request.form['yourname']
	age=request.form['yourage']
	ninja=request.form['ninja']
	if name and age and ninja:
		return render_template('profile_page.html',name=name,age=age)
	else:
		return render_template('error_page.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
	app.run()
