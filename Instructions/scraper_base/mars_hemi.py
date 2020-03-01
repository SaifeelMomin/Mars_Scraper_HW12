import requests 
from bs4 import BeautifulSoup


hemis = ['https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced', 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced',
            'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced', 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced']

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

test = hemi_scraper()      
print(test)



# hemi1 = requests.get('https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced').text
# hemi2 = requests.get('https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced').text
# hemi3 = requests.get('https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced').text
# hemi4 = requests.get('https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced').text
# soup1 = BeautifulSoup(hemi1, "html.parser")
# soup2 = BeautifulSoup(hemi2, "html.parser")
# soup3 = BeautifulSoup(hemi3, "html.parser")
# soup4 = BeautifulSoup(hemi4, "html.parser")
# img_str = soup1.find("div", "content")
# print(img_str.find("h2", class_= "title").text)




# * Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

# * You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.

# * Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.

# * Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

# *BONUS Start: There are some bugs with request whereby it doesn't wait for the whole page to load here. 
# 	      As a bonus, you can try to use Selenium (preferred) or Splinter to get all four links. 