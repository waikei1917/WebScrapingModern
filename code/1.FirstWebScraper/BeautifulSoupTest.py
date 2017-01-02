from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def beautifulSoupTest():
    html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
    bsObj = BeautifulSoup(html.read(), "html.parser")

    if True:
        print(bsObj.h1)
        print(bsObj.html.body.h1)
        print(bsObj.body.h1)
        print(bsObj.html.h1)

beautifulSoupTest()