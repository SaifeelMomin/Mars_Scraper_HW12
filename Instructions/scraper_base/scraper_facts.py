import requests 
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd 

url = 'http://space-facts.com/mars/'
file_path = "mars_facts.html"

dfs = pd.read_html(url)
df = dfs[0]
df_html = df.to_html()
print(df_html)