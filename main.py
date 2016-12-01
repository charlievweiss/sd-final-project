"""Skateboard web app developed using MVC framework (eventually compatible with WSGI for deployment)"""

from flask import Flask,render_template,request
import board_math
import hexdraw

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
	if rider_weight and riding_style:
		# Call board_math.py to get board parameters
		# Returns list of small circle diameter, big circle diameter
		riding_style = int(riding_style) #necessary to pass to board_math
		Outputs = board_math.board_math(rider_weight,riding_style)
		# TODO: next 2 lines as things in Outputs
		diameter1 = Outputs[0]
		diameter2 = Outputs[1]
		print diameter1,diameter2
		# Call hexdraw.py to generate DXF
		filename = hexdraw.hexdraw(diameter1,diameter2)
		# TODO: Convert filename DXF to an actually presentable thing.
		# the return statement should be Andrew's code
		return render_template('downloadpage.html', filename=filename)
	else:
		return render_template('error_page.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html', name=name)

if __name__ == '__main__':
	app.run()
