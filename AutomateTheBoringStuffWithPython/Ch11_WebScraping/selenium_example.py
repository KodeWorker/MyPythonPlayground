from selenium import webdriver

browser = webdriver.Firefox(executable_path='C:/Program Files/Mozilla Firefox/geckodriver.exe') # Download the geckodriver: https://github.com/mozilla/geckodriver/releases
browser.get('http://inventwithpython.com')
linkElem = browser.find_element_by_link_text('Read It Online')
linkElem.click() # follows the "Read It Online" link

