"""Skateboard web app developed using MVC framework (eventually compatible with WSGI for deployment)"""

from flask import Flask,render_template,request, redirect, url_for, send_from_directory
import board_math
import hexdraw
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = '/home/charlie/softdes/sd-final-project'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'DXF'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# main page - accepts user riding preferences
@app.route('/')
def index():
	return render_template('main_page.html')

# display page - provides board visual and downloadable file
# TODO - incorporate loading page, updating view of board
@app.route('/login',methods=['POST'])
def login():
	rider_weight=request.form['rider_weight']
	riding_style=request.form['riding_style']
	if rider_weight and riding_style:
		# Call board_math.py to get board parameters
		# Returns list of small circle diameter, big circle diameter
		rider_weight = int(rider_weight) #TODO: check if can make original inputs ints
		riding_style = int(riding_style)
		Outputs = board_math.board_math(rider_weight,riding_style)
		diameter1 = Outputs[0]
		diameter2 = Outputs[1]
		# Call hexdraw.py to generate DXF
		filename = hexdraw.hexdraw(diameter1,diameter2)
		# TODO: Convert filename DXF to an actually presentable thing.
		filename = 'http://127.0.0.1:5000/uploads/' + filename
		return render_template('downloadpage.html', filename=filename)
	else:
		return render_template('error_page.html')

# from Andrew
@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
	app.run()
