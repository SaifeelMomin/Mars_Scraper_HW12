import requests 
from bs4 import BeautifulSoup
from selenium import webdriver

html_weather = requests.get('https://twitter.com/marswxreport?lang=en').text
soup_weather = BeautifulSoup(html_weather, "html.parser")
tweets = soup_weather.find_all("div", class_ = "js-tweet-text-container")
mars_weather = tweets[0].find("p", class_ = "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
print(mars_weather)


# url = 'https://twitter.com/marswxreport?lang=en'
# file_path = "mars_weather1.html"

# driver = webdriver.Firefox()
# driver.get(url)
# html = driver.page_source
# driver.close()

# html = requests.get(url).text

# with open(file_path, "w+") as f:
#     f.write(html)

# with open(file_path, "r") as f:
#     html = f.read()

# soup = BeautifulSoup(html, "html.parser")
# tweets = soup.find_all("div", class_ = "js-tweet-text-container")
# mars_weather = tweets[0].find("p", class_ = "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
# print(mars_weather)