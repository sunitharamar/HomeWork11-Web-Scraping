# coding: utf-8
#get_ipython().system('pip install splinter ')
#from IPython import get_ipython
 
# Dependencies
# https://splinter.readthedocs.io/en/latest/drivers/chrome.html
from splinter import Browser
from bs4 import BeautifulSoup

import requests
import pymongo
import re
 
def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    # create 'mars_scrape_data' dict that we can insert into mongo
    mars_scrape_data = []


    # # NASA Mars News
    #   Scrape the "NASA Mars News Site"(http://mars.nasa.gov/news/) and collect the latest News Title and Paragragh Text. 
    #      Assign the text to variables that you can reference later.
    #      
    # ## Example:
    # news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"
    # 
    # news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, 
    #on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary 
    #launch in history from America's West Coast."
 
    # Initialize PyMongo to work with MongoDBs
    #conn = 'mongodb://localhost:27017'
   # client = pymongo.MongoClient(conn)
    

    # Define database and collection
    #db = client.nasa_news
    #collection = db.misson_to_mars

    
    # Retrieve page with the requests module
    url = 'http://mars.nasa.gov/news/'
    response = requests.get(url)
    
    # Create BeautifulSoup object; parse with 'lxml'
    soup = BeautifulSoup(response.text, 'lxml')
    

    # Print formatted version of the soup, this will give the entire page of the url to get all the details
    #print(soup.prettify())
    

    # on a new web browser the url is automatically launched with the chrome driver, please observe. very awesome!
    #Automated Selenium, chrome drive and splinter does this automation.


    url = 'http://mars.nasa.gov/news/'
    browser.visit(url)
    
    #collect the latest News Title and assign it to a variable
    news_title = soup.find('div', class_='content_title')
    news_title = news_title.a.text.strip()

    #print('-----------------')
    #print(news_title)

    

    #Get the latest news paragraph and assign it to variable
    news_p = soup.find('div', class_='rollover_description')
    news_p = news_p.text.strip()

    #print(news_p)



    # # JPL Mars Space Images - Featured Image
    # Visit the url for JPL's Featured Space Image here"https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars".
    # 
    # Use splinter to navigate the site and find the image url for the current 
    #Featured Mars Image and assign the url string to a variable called featured_image_url.
    # 
    # Make sure to find the image url to the full size .jpg image.
    # 
    # Make sure to save a complete url string for this image.
    # 
    # ## Example:
    # featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'
    
    #URL of page to be scraped
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    

    # Retrieve page with the requests module
    response = requests.get(url)

    
    # Create BeautifulSoup object; parse with 'lxml'
    soup = BeautifulSoup(response.text, 'lxml')
    
    # Print formatted version of the soup, this will give the entire page of the url to get all the details
    #print(soup.prettify())
    
    href = soup.find('a', class_='button fancybox')
    #print(href)
    


    href['data-fancybox-href']

    
    featured_image_url = 'https://www.jpl.nasa.gov/' + href['data-fancybox-href']
    #print(featured_image_url)


    # # Mars Weather
    # Visit the Mars Weather twitter account here"https://twitter.com/marswxreport?lang=en" and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called mars_weather.
    # ## Example:
    # mars_weather = 'Sol 1801 (Aug 30, 2017), Sunny, high -21C/-5F, low -80C/-112F, pressure at 8.82 hPa, daylight 06:09-17:55'
    
    #URL of page to be scraped
    url = 'https://twitter.com/marswxreport?lang=en'
    
    # Retrieve page with the requests module
    response = requests.get(url)
    
    # Create BeautifulSoup object; parse with 'lxml'
    soup = BeautifulSoup(response.text, 'lxml')
    
    # Print formatted version of the soup, this will give the entire page of the url to get all the details
    #print(soup.prettify())
    
    mars_weather = soup.find('div',  class_="js-tweet-text-container").get_text()
    #print(mars_weather)


    # # Mars Facts
    # Visit the Mars Facts webpage here"https://space-facts.com/mars/" and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    # 
    # Use Pandas to convert the data to a HTML table string.
    # ## Scraping with Pandas
    # 
    
    import pandas as pd

    
    #We can use the read_html function in Pandas to automatically scrape any tabular data from a page.
    
    url = 'https://space-facts.com/mars/'
    

    tables = pd.read_html(url)
    tables
    
    #What we get in return is a list of dataframes for any tabular data that Pandas found.
    
    type(tables)

    
    #We can slice off any of those dataframes that we want using normal indexing.
    
    df = tables[0]
    df.columns = ['Description', 'Value' ]
    df
    
    #Set the index to the Description column
    
    df.set_index('Description', inplace=True)
    df

    
    df.loc['Recorded By:']


    # # DataFrames as HTML
    
    #Pandas also had a to_html method that we can use to generate HTML tables from DataFrames.
    
    html_table = df.to_html()
    html_table
    
    #You may have to strip unwanted newlines to clean up the table.
    facts_table = html_table.replace('\n', '')
    facts_table
    

    #You can also save the table directly to a file.
    
    df.to_html('table.html')
    
    # OSX Users can run this to open the file in a browser, 
    # or you can manually find the file and open it in the browser
    #get_ipython().system('open table.html   #Wow! very cool')


    # # Mars Hemisperes
    # Visit the USGS Astrogeology site here"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars" to obtain high resolution images for each of Mar's hemispheres.
    # 
    # You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
    # 
    # Save both the image url string for the full resolution hemipshere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
    # 
    # Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.
    # 
    # ## Example:
    # hemisphere_image_urls = [
    #     {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    #     {"title": "Cerberus Hemisphere", "img_url": "..."},
    #     {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    #     {"title": "Syrtis Major Hemisphere", "img_url": "..."},
    # ]
    

    # URL of page to be scraped
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    
    browser.visit(url)

    # Retrieve page with the requests module
    response = requests.get(url)
    # Create BeautifulSoup object; parse with 'lxml'
    soup = BeautifulSoup(response.text, 'lxml')

    hemisphere_image_urls = []
    results = soup.find_all('a', class_='itemLink product-item')
    for result in results:
        #print("=================")
        
        hemisphere_title = result.find('h3').get_text()
        #print(hemisphere_title)
        
        new_url = "https://astrogeology.usgs.gov" + result['href']
        browser.visit(new_url)
        #print(new_url)
        
        # Retrieve page with the requests module
        response2 = requests.get(new_url)
    
        browser2 = Browser('chrome', headless=False)
        soup2 = BeautifulSoup(response2.text, 'lxml')
        
        next_page = soup2.find('div', class_='downloads')
        #print(next_page)
        
        
        link = next_page.find('a')['href']
        #print(link)
        hemisphere_url = link
        #print("This is ")
        #print(hemisphere_url)
        
        hemisphere_image_urls.append({'title': hemisphere_title, 'img_url': hemisphere_url})

    #print("=====================================================")
    #print(hemisphere_image_urls)
    #print("=====================================================")
    

    #hemisphere_image_urls


    # # Step 2 - MongoDB and Flask Application
    # Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.
    # 
    # Start by converting your Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.
    # 
    # Next, create a route called /scrape that will import your scrape_mars.py script and call your scrape function.
    # 
    # Store the return value in Mongo as a Python dictionary.
    # Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.
    # 
    # Create a template HTML file called index.html that will take the mars data dictionary and display all 
    #of the data in the appropriate HTML elements. Use the following as a guide for what the final product 
    #should look like, but feel free to create your own design.
    

    # Create a dictionary with all of the above scraped variables 
    mars_scrape_data = {'hemispheres': hemisphere_image_urls,
                        'facts': facts_table,
                        'mars_weather': mars_weather,
                        "featured_image_url": featured_image_url,
                        'news_title': news_title,
                        'news_text': news_p}

    mars_scrape_data

    return mars_scrape_data

#results = {}
#results = scrape()
#print(results)
        
        