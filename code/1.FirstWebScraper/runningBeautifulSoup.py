from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def beautifulSoupTest():
    html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
    bsObj = BeautifulSoup(html.read(), "html.parser")

    if False:
        print(bsObj.h1)
        print(bsObj.html.body.h1)
        print(bsObj.body.h1)
        print(bsObj.html.h1)

beautifulSoupTest()


def getTitle(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        return None

    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None

    return title

title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html")
if title == None:
    print("page could not be found")
else:
    print(title)











