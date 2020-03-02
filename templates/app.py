from flask import Flask, request, redirect, render_template
import requests 
from flask_pymongo import PyMongo
from mars_scraper import scraper, scraper_s


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

def scrape_type(x):
    mongo.db.mars_info.drop()
    collection = mongo.db.mars_info
    if x == 's':
        collection.insert_one(scraper_s())
    elif x == "r":
        collection.insert_one(scraper())
    else: pass

@app.before_first_request
def init_app():
    scrape_type("r")

@app.route("/scrape", methods=['GET', 'POST'])
def data_scrape():
    if request.method == "POST":        
        scrape_type("r")
        return redirect("/")
    else: 
        return redirect("/")

@app.route("/")
def landing():
    try:
        page_data = mongo.db.mars_info.find()[0]
    except: 
        scrape_type("r")
        page_data = mongo.db.mars_info.find()[0]
    return render_template("index.html", marsData = page_data)


@app.route("/hemispheres")
def hemispheres():
    try:
        page_data = mongo.db.mars_info.find()[0]
    except: 
        scrape_type("r")
        page_data = mongo.db.mars_info.find()[0]
    return render_template("hemi.html", marsData = page_data)


if __name__ == "__main__":
    app.run(debug = True)

