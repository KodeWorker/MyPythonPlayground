"""
Automate the Boring Stuff with Python
Chapter 11 Web Scraping - Project: 2048
Description:
    2048 is a simple game where you combine tiles by sliding them up,
    down, left, or right with the arrow keys. You can actually get a
    fairly high score by repeatedly sliding in an up, right, down,
    and left pattern over and over again. Write a program that will
    open the game at https://gabrielecirulli.github.io/2048/ and keep
    sending up, right, down, and left keystrokes to automatically play
    the game.
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox(executable_path='C:/Program Files/Mozilla Firefox/geckodriver.exe') # Download the geckodriver: https://github.com/mozilla/geckodriver/releases
browser.get('https://gabrielecirulli.github.io/2048/')

# The <html> tag is the base tag in HTML files: The full content of the HTML file is enclosed within the <html> and </html> tags
htmlElem = browser.find_element_by_tag_name('html')

play = True

while play:
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.LEFT)
    try:
        browser.find_element_by_css_selector('div .game-message.game-over')
        play = False
    except:
        print('continue playing...')    
    
print('Game Over!')
