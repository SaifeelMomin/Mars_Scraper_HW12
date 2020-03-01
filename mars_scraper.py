# Dependencies 
import requests 
import urllib.parse
from bs4 import BeautifulSoup
import datetime as dt
import pandas as pd



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
    # mars_weather = tweets[0].find("p", class_ = "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    mars_weather = (tweets[0].p.next_element)
    mars_dict['weather'] = mars_weather.strip()

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

    # # TIMESTAMP
    # ts = time.time()
    # mars_dict['id'] = ts
    
    return mars_dict
