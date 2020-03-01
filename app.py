from flask import Flask, request, jsonify, render_template
import pandas as pd
import requests 
import urllib.parse
from bs4 import BeautifulSoup
from flask_pymongo import PyMongo
from mars_scraper import scraper


app = Flask(__name__)

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

@app.before_first_request
def init_app():
    data = scraper()
    mongo.db.mars_info.drop()
    collection = mongo.db.mars_info
    collection.insert_one(data)

@app.route("/scrape", methods=['GET', 'POST'])
def data_scrape():
    if request.method == "POST":        
        data = scraper()
        mongo.db.mars_info.drop()
        collection = mongo.db.mars_info
        collection.insert_one(data)
        # db_size = mongo.db.mars_info.count()
        page_data = mongo.db.mars_info.find()[0]
        return render_template("index.html", news_title=page_data['news'][1], news_p = page_data['news'][1], featured_img = page_data['img'], 
                                facts = page_data['facts'], weather = page_data['weather'])
    else: 
        db_size = mongo.db.mars_info.count()
        page_data = mongo.db.mars_info.find()[db_size-1]
        return render_template("index.html", news_title=page_data['news'][1], news_p = page_data['news'][1], featured_img = page_data['img'], 
                                facts = page_data['facts'], weather = page_data['weather'])

##################################################  USE SELENIUM TO GET NASA NEWS INFO????    ###################################################################
@app.route("/")
def landing():
    # db_size = mongo.db.mars_info.count()
    page_data = mongo.db.mars_info.find()[0]

    # hemi1 = page_data['hemisphere_data']['hemi1']
    # hemi2 = page_data['hemisphere_data']['hemi2']
    # hemi3 = page_data['hemisphere_data']['hemi3']
    # hemi4 = page_data['hemisphere_data']['hemi4']

    return render_template("index.html", news_title=page_data['news'][1], news_p = page_data['news'][1], 
                            featured_img = page_data['img'], facts = page_data['facts'], weather = page_data['weather'])

# @app.route("/")
# def hemispheres():

if __name__ == "__main__":
    app.run(debug = True)



# Next, create a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.

# Store the return value in Mongo as a Python dictionary.

# Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display 