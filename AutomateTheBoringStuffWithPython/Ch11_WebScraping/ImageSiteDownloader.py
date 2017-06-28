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

search = ''
while len(search) == 0: 
    search = input('Please enter search topic:\n')

url = 'https://www.flickr.com' # url
os.makedirs(search, exist_ok=True)

print('Downloading page of "%s"...' %(search))
browser = webdriver.Firefox(executable_path='C:/Program Files/Mozilla Firefox/geckodriver.exe')
browser.get('%s/search/?text=%s' %(url, search))
delay = 3

WebDriverWait(browser, delay).until(EC.presence_of_element_located(browser.find_element_by_id('...')))

elements = soup.select('body #content main .main.search-photos-results \
                .view.photo-list-view.requiredToShowOnServer \
                .view.photo-list-photo-view.requiredToShowOnServer.awake \
                .interaction-view')

print(elements)                
# Get the link to each results
