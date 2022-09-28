
from flask import Flask, render_template 
import csvtodata
app = Flask(__name__)
#THE root page
@app.route('/')
def main():
	return render_template("main.html")
@app.route('/Home')
def home():
	return render_template("main.html")
@app.route('/About')
def about():
	return render_template("about.html")
@app.route('/Contact')
def contact():
	return render_template("contact.html")
@app.route('/Attendances')
def display_data(): 
   
    attendance_d = csvtodata.get_data() #data from database 
#render_template : tool for displaying data with html file
    return render_template("attendances.html", value=attendance_d) 
if __name__ == "__main__":
	app.run(debug=True , host= '0.0.0.0')
