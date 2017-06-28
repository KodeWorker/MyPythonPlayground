# Notes

## Don't use regular expressions to parse HTML

Locating a specific piece of HTML in a string seems like a perfect case for regular expressions. However, I advise you against it. There are many different ways that HTML can be formatted and still be considered valid HTML, but trying to capture all these possible variations in a regular expression can be tedious and error prone. A module developed specifically for parsing HTML, such as Beautiful Soup, will be less likely to result in bugs.

You can find an extended argument for why you shouldn’t to parse HTML with regular expressions at http://stackoverflow.com/a/1732454/1893164/

## Beautiful Soup 4

[1] Use requests.get(URL) to download the page of URL -> pass the text attribute to bs4.BeautifulSoup()

[2] For downloaded HTML, us open('XXX.html')

[3] Finding element with select() method: passing a string of a CSS selector for the element you are looking for.

## Selenium Module

[1] Download the geckodriver for Firefox: https://github.com/mozilla/geckodriver/releases

[2] browser = webdriver.Firefox(executable_path='C:/Program Files/Mozilla Firefox/geckodriver.exe')

## Other problems

[1] Beautiful Soup returns incomplete HTML on Flickr: the content is loaded via javascript -> use selenium
    reference: https://stackoverflow.com/questions/41706274/beautifulsoup-returns-incomplete-html
