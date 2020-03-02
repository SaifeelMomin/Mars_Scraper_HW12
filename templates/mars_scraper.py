# Dependencies 
import requests 
import urllib.parse
from bs4 import BeautifulSoup
import datetime as dt
import pandas as pd
from selenium import webdriver 
def news_scrape():
    news = {}
    html_news = requests.get("https://mars.nasa.gov/news/").text
    soup_news = BeautifulSoup(html_news, "html.parser")    
    slides = soup_news.find_all("div", class_ = "slide")
    news_title = slides[0].find("div", class_ = "content_title").text
    news_p = slides[0].find("div", class_ = "rollover_description_inner").text
    news_url = urllib.parse.urljoin("https://mars.nasa.gov/news", slides[0].a["href"])
    news["title"] = news_title
    news["sub_title"] = news_p
    news["url"] = news_url
    return news

def news_scrape_s(d):
    news = {}
    d.get('https://mars.nasa.gov/news/')
    html = d.page_source
    soup = BeautifulSoup(html, "html.parser")    
    slides = soup.find_all("li", class_ = "slide")
    news_title = slides[0].find("div", class_ = "content_title").text
    news_p = slides[0].find("div", class_ = "rollover_description_inner").text
    news_url = urllib.parse.urljoin("https://mars.nasa.gov/news", slides[0].a["href"])
    news["title"] = news_title
    news["sub_title"] = news_p
    news["url"] = news_url
    return news 

def img_scrape():
    ft_img = {}
    html_img = requests.get('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars').text
    soup_img = BeautifulSoup(html_img, "html.parser")    
    articles = soup_img.find("article", class_ = "carousel_item")
    img_link = articles.a["data-fancybox-href"]
    featured_image_url = urllib.parse.urljoin("https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars", img_link)
    ft_img["img"] = featured_image_url
    return ft_img

def weather_scrape():
    weather = {}
    html_weather = requests.get('https://twitter.com/marswxreport?lang=en').text
    soup_weather = BeautifulSoup(html_weather, "html.parser")
    tweets = soup_weather.find_all("div", class_ = "js-tweet-text-container")
    mars_weather = (tweets[0].p.next_element)
    weather['weather'] = mars_weather.strip()
    return weather 

def fact_scrape():
    facts = {}
    dfs = pd.read_html('http://space-facts.com/mars/')
    df = dfs[0]
    df = df.rename({0: " ", 1: "Value"}, axis = 1)
    df = df.set_index(" ")
    df_html = df.to_html() 
    facts["fact"] = df_html
    return facts 

def hemi_scrape():
    hemi_list = ['https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced', 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced',
                    'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced', 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced']  
    hemispheres = [] 
    for hemi in hemi_list:
        hemi_dict = {}
        html = requests.get(hemi).text
        soup = BeautifulSoup(html, "html.parser")
        img_link = soup.find("div", "downloads")
        img_str = soup.find("div", "content")
        title = img_str.find("h2", class_= "title").text
        hemi_dict['title'] = title
        hemi_dict['img_url'] = img_link.a["href"]
        hemispheres.append(hemi_dict)
    return hemispheres

def hemi_scrape_s(d):
    hemi_list = ['https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced', 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced',
                    'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced', 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced']
    hemispheres = [] 
    for hemi in hemi_list:
        hemi_dict = {}
        d.get(hemi)
        html = d.page_source
        soup = BeautifulSoup(html, "html.parser")
        img_link = soup.find("div", "downloads")
        img_str = soup.find("div", "content")
        title = img_str.find("h2", class_= "title").text
        hemi_dict['title'] = title
        hemi_dict['img_url'] = img_link.a["href"]
        hemispheres.append(hemi_dict)
    d.close()
    return hemispheres

## using requests 
def scraper():
    mars_data = {}
    data = [["news", news_scrape()], ["hemispheres", hemi_scrape()], ["img", img_scrape()], ["weather", weather_scrape()], ["facts", fact_scrape()]]
    for e in data:
        mars_data[e[0]] = e[1]
    return mars_data

## using selenium 
def scraper_s():
    mars_data = {}
    driver = webdriver.Firefox()
    data = [["news", news_scrape_s(driver)], ["img", img_scrape()], ["weather", weather_scrape()], ["facts", fact_scrape()], ["hemispheres", hemi_scrape_s(driver)]]
    for e in data:
            mars_data[e[0]] = e[1]
    return mars_data
    

 