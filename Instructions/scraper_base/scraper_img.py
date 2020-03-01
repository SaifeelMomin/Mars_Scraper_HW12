import requests 
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.parse


url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
file_path = "mars_img.html"

# driver = webdriver.Firefox()
# driver.get(url)
# html = driver.page_source
# driver.close()

# with open(file_path, "w+") as f:
#     f.write(html)
with open(file_path, "r") as f:
    html = f.read()


soup = BeautifulSoup(html, "html.parser")    
articles = soup.find("article", class_ = "carousel_item")

# for article in articles:
#     try:
#         img_link = article.a["data-fancybox-href"]
#         featured_image_url = urllib.parse.urljoin("https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars", img_link)
#         print("------------------")
#         print(featured_image_url)
#     except AttributeError as e:
#         print(e)
img_link = articles.a["data-fancybox-href"]
featured_image_url = urllib.parse.urljoin("https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars", img_link)
print("------------------")
print(featured_image_url)