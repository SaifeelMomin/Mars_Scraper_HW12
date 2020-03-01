# Dependencies 
import requests 
import urllib.parse
from bs4 import BeautifulSoup
# from selenium import webdriver
import pandas as pd
# import pymongo 


# Initialize PyMongo to work with MongoDBs
# conn = "mongodb://localhost:27017"
# client = pymongo.MongoClient(conn)

# Define database and collection
# db = client.mars_db
# collection = db.marsData

def hemi_scraper():
    hemi_list = ['https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced', 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced',
                    'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced', 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced']  
    hemisphere_data = {}
    count = 0 
    for hemi in hemi_list:
        html = requests.get(hemi).text
        soup = BeautifulSoup(html, "html.parser")
        img_link = soup.find("div", "downloads")
        img_str = soup.find("div", "content")
        title = img_str.find("h2", class_= "title").text
        count += 1
        hemisphere_data[f"hemi{count}"] = [title, img_link.a["href"]]
    return hemisphere_data


def scraper():
    mars_dict = {}
    # NEWS SCRAPE 
    html_news = requests.get("https://mars.nasa.gov/news/").text
    soup_news = BeautifulSoup(html_news, "html.parser")    
    slides = soup_news.find_all("div", class_ = "slide")
    news_title = slides[0].find("div", class_ = "content_title").text
    news_p = slides[0].find("div", class_ = "rollover_description_inner").text
    mars_dict['news'] = [news_title.strip(), news_p.strip()]


    # IMG SCRAPE 
    html_img = requests.get('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars').text
    soup_img = BeautifulSoup(html_img, "html.parser")    
    articles = soup_img.find("article", class_ = "carousel_item")
    img_link = articles.a["data-fancybox-href"]
    featured_image_url = urllib.parse.urljoin("https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars", img_link)
    mars_dict['img'] = featured_image_url
    
    # WEATHER SCRAPE 
    html_weather = requests.get('https://twitter.com/marswxreport?lang=en').text
    soup_weather = BeautifulSoup(html_weather, "html.parser")
    tweets = soup_weather.find_all("div", class_ = "js-tweet-text-container")
    mars_weather = tweets[0].find("p", class_ = "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    mars_dict['weather'] = mars_weather

    # FACTS SCRAPE 
    dfs = pd.read_html('http://space-facts.com/mars/')
    df = dfs[0]
    df = df.rename({0: " ", 1: "Value"}, axis = 1)
    df = df.set_index(" ")
    df_html = df.to_html() 
    mars_dict['facts'] = df_html

    # HEMISPHERES SCRAPE 
    hemisphere_data = hemi_scraper()
    mars_dict["hemisphere_data"] = hemisphere_data

    return mars_dict

mars_data = scraper()    
hemi1_lnk = mars_data['hemisphere_data']['hemi1'][0]
hemi1 = mars_data['hemisphere_data']['hemi1'][1] 

print(hemi1_lnk, hemi1)

# collection.insert_one(test)

# listing = db.marsData.find()[0]
# print(listing['news'])


# # BASE URLS FOR SCRAPE 
# url_news = "https://mars.nasa.gov/news/"
# url_img = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
# url_weather = 'https://twitter.com/marswxreport?lang=en'
# url_facts = 'http://space-facts.com/mars/'


# # HTML SOURCE CODE 
# html_news = r.get(url_news).text
# html_img = r.get(url_img).text
# html_weather = r.get(url_weather).text

# # NEWS SCRAPE 
# soup_news = BeautifulSoup(html_news, "html.parser")    
# slides = soup_news.find_all("li", class_ = "slide")
# news_title = slides[0].find("div", class_ = "content_title").text
# news_p = slides[0].find("div", class_ = "rollover_description_inner").text

# # IMG SCRAPE 
# soup_img = BeautifulSoup(html_img, "html.parser")    
# articles = soup_img.find("article", class_ = "carousel_item")
# img_link = articles.a["data-fancybox-href"]
# featured_image_url = urllib.parse.urljoin("https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars", img_link)


# # WEATHER SCRAPE 
# soup_weather = BeautifulSoup(html_weather, "html.parser")
# tweets = soup_weather.find_all("div", class_ = "js-tweet-text-container")
# mars_weather = tweets[0].find("p", class_ = "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")


# # FACTS SCRAPE 
# dfs = pd.read_html(url_facts)
# df_facts = dfs[0]
# df_facts_html = df_facts.to_html()

# # DICT WITH ALL SCRAPED DATA
# mars_dict = {}
# mars_dict['news'] = [news_title, news_p]
# mars_dict['img'] = featured_image_url
# mars_dict['weather'] = mars_weather
# mars_dict['facts'] = df_facts_html