import requests 
from bs4 import BeautifulSoup
from selenium import webdriver
test_dict = {}
html_news = requests.get("https://mars.nasa.gov/news/").text
soup_news = BeautifulSoup(html_news, "html.parser")    
slides = soup_news.find_all("div", class_ = "slide")
news_title = slides[0].find("div", class_ = "content_title").text
news_p = slides[0].find("div", class_ = "rollover_description_inner").text
test_dict['news'] = [news_title.strip(), news_p.strip()]
print(test_dict)

# url = "https://mars.nasa.gov/news/"
# file_path = "nasa_mars.html"

# driver = webdriver.Firefox()
# driver.get(url)
# driver.implicitly_wait(20)
# html = driver.page_source
# driver.close()



# with open(file_path, "w+") as f:
#     f.write(html)

# with open(file_path, "r") as f:
#     html = f.read()


# soup = BeautifulSoup(html, "html.parser")    
# slides = soup.find_all("li", class_ = "slide")

# for slide in slides:
#     try:
#         title = slide.find("div", class_ = "content_title").text
#         sub = slide.find("div", class_ = "rollover_description_inner").text
#         print("------------------")
#         print(title)
#         print(sub)
#     except AttributeError as e:
#         print(e)
# news_title = slides[0].find("div", class_ = "content_title").text
# news_p = slides[0].find("div", class_ = "rollover_description_inner").text
# print(news_title)
# print(news_p)