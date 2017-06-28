import requests


def Main():
    url = 'http://www.gutenberg.org/cache/epub/1112/pg1112.txt'
#    url = 'http://www.gutenberg.org/cache/epub/1112/pg1112-images.html'
#    url = 'http://inventwithpython.com/page_that_does_not_exist'
    res = requests.get(url)
    try:
        res.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' %(exc))
    
    cachesize = 1000
    
    with open('RomeoAndJuliet.txt', 'wb') as playFile:
        for chunk in res.iter_content(cachesize):
            if len(chunk) % cachesize != 0:
                chunk += b' ' * ( cachesize - len(chunk))
            playFile.write(chunk)
            
if __name__ == '__main__':
    Main()