"""main page for app
- assigns upload folder for DXF
- takes inputs from user by accessing main_page.html
- calls board_math.py and hexdraw.py to calculate specs and create DXF
- provides link to DXF download on downloadpage.html

TODO:
- make DXF upload happen non-locally
- convert DXF to viewable file
- change main_page.html to make original inputs ints rather than converting here"""

from flask import Flask,render_template,request, redirect, url_for, send_from_directory
import board_math
import hexdraw
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
# configure folder for upload
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'DXF'])
# present main page
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/draw')
def left_bar():
	return render_template('draw.html')

# present download page
@app.route('/download',methods=['POST'])
def download():
	# accept user inputs from main_page.html (which points here)
	rider_weight=request.form['rider_weight']
	riding_style=request.form['riding_style']
	if rider_weight and riding_style:
		if rider_weight < 90 or rider_weight > 300:
			# Call board_math.py to get board parameters
			# Returns list of small circle diameter, big circle diameter
			rider_weight = int(rider_weight) #TODO: check if can make original inputs ints
			riding_style = int(riding_style)
			#Outputs = board_math.board_math(rider_weight,riding_style)
			# Call hexdraw.py to generate DXF
			filename = hexdraw.hexdraw(Outputs[0],Outputs[1])
			# Make filename access file at this location -- see below @app.route('/uploads/<filename>')
			filename = 'http://127.0.0.1:5000/static/' + filename
			return render_template('download.html', filename=filename)
	else:
		return render_template('error.html')

# upload DXF file
@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

app.run(threaded=True)
