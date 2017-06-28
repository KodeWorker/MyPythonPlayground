"""
Automate the Boring Stuff with Python
Chapter 11 Web Scraping - Project: "I'm Feeling Lucky" Google Search
Description:
    It would be nice if I could simply type a search term on the command
    line and have my computer automatically open a browser with all the
    top search results in new tabs. Let’s write a script to do this.
    
    - Gets search keywords from the command line arguments.
    - Retrieves the search results page.
    - Opens a browser tab for each result.
"""

import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()


# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)

# Open a browser tab for each result.
linkElems = soup.select('.r a') #  to find all <a> elements that are within an element that has the r CSS class

numOpen = min(5, len(linkElems))

for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))