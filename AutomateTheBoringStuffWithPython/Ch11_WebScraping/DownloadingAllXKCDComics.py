"""
Automate the Boring Stuff with Python
Chapter 11 Web Scraping - Project: Downloading All XKCD Comics
Description:
    If you wanted a copy of the site’s content to read when you’re 
    not online, you could manually navigate over every page and
    save each one. But this is pretty boring work, so let’s write
    a program to do it instead.
    
    - Loads the XKCD home page.
    - Saves the comic image oon the page
    - Follows the previous comic link
    - Repeats until it reaches the first comic
"""
import requests, os, bs4

url = 'http://xkcd.com' # starting url
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    try:
        # Download the web page
        print('Downloading page %s...' %(url))
        res = requests.get(url)
        res.raise_for_status()
    except Exception as exc:
        # Get the Prev button's url
        prevLink = soup.select('a[rel="prev"]')[0] # identifies the <a> element with the rel attribute set to prev
        url = 'http://xkcd.com' + prevLink.get('href')   
        
    soup = bs4.BeautifulSoup(res.text)
    # Find and download the comic image
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicURL = 'http:' + comicElem[0].get('src') # little bit different
        # Download the image
        print('Downloading image %s...' %(comicURL))
        res = requests.get(comicURL)
        res.raise_for_status()
        
        # Save the image to ./xkcd
        with open(os.path.join('xkcd', os.path.basename(comicURL)), 'wb') as imageFile:
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
        
print('Done.')
