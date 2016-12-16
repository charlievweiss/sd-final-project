"""Main page for app
- assigns upload folder for DXF
- takes inputs from user by accessing index.html
- calls board_math.py and hexdraw.py to calculate specs and create DXF
- provides link to DXF download on download.html
"""

from flask import Flask,render_template,request, redirect, url_for, send_from_directory
import board_math
import hexdraw


app = Flask(__name__)
# configure folder for upload
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['DXF']) #List of allowed extensions. We only want DXF files.
# present main page
@app.route('/')
def index(): #Uses flask to render the homepage
	return render_template('index.html')

@app.route('/form')
def left_bar(): #Renders the form and routes it to '/form'
	return render_template('form.html')

"""
Takes in user input from form.html, checks that it is a valid entry, 
generates a model based on the information, and sends the user to the download 
page if valid.
"""
@app.route('/download',methods=['POST'])
def download():
	rider_weight=request.form['rider_weight']
	riding_style=request.form['riding_style']
	if rider_weight and riding_style:
			try: #tests to see if the input returns an error of any kind and if so defaults to except
				if float(rider_weight)<=900 and float(rider_weight) >= 20:
					# Call board_math.py to get board parameters
					rider_weight = int(rider_weight) 
					riding_style = int(riding_style)
					Outputs = board_math.board_math(rider_weight,riding_style) #Returns list of small circle diameter, big circle diameter
					filename ='http://127.0.0.1:5000/static/' + hexdraw.hexdraw(Outputs[0],Outputs[1]) # Call hexdraw.py to generate DXF and modify the filename to refer to the local window
					return render_template('download.html', filename=filename) #render the download page, which references filename
				else:
					return render_template('error.html') #returns the error page if the weight is too large or too small
			except:
				return render_template('error.html') #returns the error page if any other issue occurs (ex. if the user enters "cat")
	else:
		return render_template('error.html') #returns the error page if the user does not fill out the form in its entirety

# upload DXF file
@app.route('/uploads/<filename>') #Allows file to be uploaded and called for download on the web.
def send_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

app.run(threaded=True) #Runs the app
