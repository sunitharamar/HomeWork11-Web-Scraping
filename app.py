# This is the Flask App(app.py) Flask API, importing the python function "scrape_mars"
#(which has all the scraped data dict from the web) 
#into this app.py

#Why is Flask a good web framework choice?
#Flask is considered more Pythonic than Django because Flask web application code 
#is in most cases more explicit. Flask is easy to get started with as a beginner because 
#there is little boilerplate code for getting a simple app up and running.


#The process:
#from various sites into a dictionary and then into a mongo db.  
# After retrieving the data from mongo and passing it to your html template

# 1) Save all the scrapped data into a dictionary in "scrape_mars.py"
# 2) import "scrape_mars.py" into "app.py"(Flask app - which is a webserver API - will be listening to http requests)
# 3) Save all the python dictionary scrapped data to "MongoDB" (@app.route('/scrape')  API from flask webframe work.)
# 4) Now the Flask routes the 3) step to endpoint (@ap.route('/) for index.html file , 
#     where in all the data is rendered on a web page.

# How to run this app:
# On terminal type iptython app.py
# ex: Sunithas-MacBook-Pro:HomeWork11-Web-Scraping sunitharamakrishnan$ ipython app.py
# * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
# * Restarting with stat
 #* Debugger is active!
# * Debugger PIN: 329-477-025
# go to a web and launch this url: http://127.0.0.1:5000/   to look at the results

# Before running make sure that on a terminal: run "mongod" <-- server
# another terminal run "mongo" <-- client


from flask import Flask, render_template, jsonify, redirect
import pymongo
import scrape_mars

app = Flask(__name__)

#mongo = PyMongo(app)

# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)


# Define database and collection
# Note: Database names CANNOT be with underscores. "nasa_news" <-- DID not work earlier.
db = client.nasaNews
collection = db.missionToMars


@app.route('/')
def index():
    mission = db.missionToMars.find_one()
    print(mission)
    return render_template('index.html', mission=mission)


@app.route('/scrape')
def scrape():
    mission = db.missionToMars
    data = scrape_mars.scrape()
    mission.update({}, data, upsert=True)
    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
