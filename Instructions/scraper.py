import requests 
from bs4 import BeautifulSoup
from selenium import webdriver

url = "https://mars.nasa.gov/news/"
file_path = "nasa_mars.html"

# driver = webdriver.Firefox()
# driver.get(url)
# driver.implicitly_wait(20)
# html = driver.page_source
# driver.close()

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()


soup = BeautifulSoup(html, "html.parser")    
slides = soup.find_all("li", class_ = "slide")

for slide in slides:
    try:
        title = slide.find("div", class_ = "content_title").text
        sub = slide.find("div", class_ = "rollover_description_inner").text
        print("------------------")
        print(title)
        print(sub)
    except AttributeError as e:
        print(e)

