"""Skateboard web app developed using MVC framework (eventually compatible with WSGI for deployment)"""

from flask import Flask,render_template,request
app = Flask(__name__)

# All this is part of the Viewer

# main page - accepts user riding preferences
@app.route('/')
def index():
	return render_template('main_page.html')

# display page - provides board visual and downloadable file
# TODO - incorporate loading page, updating view of board
@app.route('/login',methods=['POST'])
def login():
	rider_weight=request.form['rider_weight']
	board_length=request.form['board_length']
	riding_style=request.form['riding_style']
	if rider_weight and board_length and riding_style:
		return render_template('profile_page.html',name=rider_weight,age=board_length)
	else:
		return render_template('error_page.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
	app.run()
