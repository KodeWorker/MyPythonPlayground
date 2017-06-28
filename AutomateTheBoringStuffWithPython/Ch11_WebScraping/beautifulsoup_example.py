import bs4
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
elems = exampleSoup.select('#author')

print(str(elems[0]))
print(elems[0].getText())
print(elems[0].attrs)