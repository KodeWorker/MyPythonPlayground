"""
Automate the Boring Stuff with Python
Chapter 11 Web Scraping - Project: Image Site Downloader
Description:
    Write a program that goes to a photo-sharing site like Flickr or Imgur,
    searches for a category of photos, and then downloads all the resulting
    images. You could write a program that works with any photo site that
    has a search feature.
"""
import os
import requests, bs4
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

search = ''
while len(search) == 0: 
    search = input('Please enter search topic:\n')

url = 'https://www.flickr.com' # url
os.makedirs(search, exist_ok=True)

print('Downloading page of "%s"...' %(search))

# Problem: Beautifulsoup returns incomplete html
# Solution: https://stackoverflow.com/questions/41706274/beautifulsoup-returns-incomplete-html

browser = webdriver.Firefox(executable_path='C:/Program Files/Mozilla Firefox/geckodriver.exe')
browser.get('%s/search/?text=%s' %(url, search))
delay = 3

WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'search-unified-content')))

soup = bs4.BeautifulSoup(browser.page_source, "html.parser")

elements = soup.select('body #content main .main.search-photos-results \
                .view.photo-list-view.requiredToShowOnServer \
                .view.photo-list-photo-view.requiredToShowOnServer.awake \
                .interaction-view \
                .title')

#print(elements)
  
# Get the link of each results in the first page of flikr
# need to find another means to download the pics of all search results!!!!!!!!!!!

for result in elements:
    picURL = 'https://www.flickr.com' + result.get('href') + 'sizes/o/in/photostream/'   
    browser.get(picURL)  
    
    # https://stackoverflow.com/questions/36789287/how-do-i-extract-just-src-with-beautiful-soup
    soup = bs4.BeautifulSoup(browser.page_source, "html.parser")
    picElem = soup.select('div[id="allsizes-photo"] img[src]')[0]
    picURL = picElem.get('src')
    
    print(picURL)
    
    res = requests.get(picURL)
    res.raise_for_status()
    
    # Save the image
    filename = os.path.basename(picURL)
    if '?' in filename:
        filename = filename[:filename.index('?')]
    
    imageFile = open(os.path.join(search, filename), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    
