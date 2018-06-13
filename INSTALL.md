# HomeWork11-Web-Scraping

Web-Scraping-and-Document-Databases
The goal is to build a web application that scrapes data related to the Mission to Mars from the following websites:

https://mars.nasa.gov/news/?page=0&per_page=15&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest
https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
https://twitter.com/marswxreport?lang=en
https://space-facts.com/mars/
and displays the information in a single HTML page.

Requirements:
beautifulsoup4==4.6.0
selenium==3.5.0
splinter==0.7.6
Flask==0.12.2
Flask-Cors==3.0.3
Flask-PyMongo==0.5.1
pandas==0.20.3
tweepy==3.5.0

How to run the app:
1) on a terminal:
    first start mongod 
    $mongod  <--- starting the mongo db server

2) on another terminal:
    second start the mongo 
   $mongo <--- starting the mongo CLI client

3) cd to the directory where your data and app is located:
    $ python app.py

4) go to a web browser and launch your url:
   http://localhost:5000/



