# Define the Imports 

from flask import Flask, render_template 
from functions import convert_html_json, free_time_slots
from bs4 import BeautifulSoup

# Open html file "MyFitness.html" 
with open ("MyFitness.html", 'rb') as html_doc:
	soup = BeautifulSoup(html_doc, 'lxml')

# Search for the all Table within the MyFitness.html file 
html_table = soup.find_all('table')[0]

# Convert the Html to Json format and save the output on data.json file 
data = convert_html_json(html_table)

# Create a Dictionary for free time slots 
free_time = free_time_slots(data)

#print(free_time)

app = Flask(__name__) 

@app.route("/")

@app.route("/home")

def home():
	return render_template('home.html', free_time=free_time)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
