import urllib.request as rq
import urllib.error as err
from bs4 import BeautifulSoup
import sys

### victim url https://store.steampowered.com/genre/Free%20to%20Play/#p=1&tab=NewReleases

def get(url):
        try:
                return rq.urlopen(url).read()
        except err.HTTPError as e:
                return None
        except err.URLError as e:
                return None
# supposidly you would loop this until you got a 404 error
def getPage(num, t="newReleases"):    
    raw_html = get("https://store.steampowered.com/genre/Free%20to%20Play/#p={}&tab={}".format(num,t))
    
    html = BeautifulSoup(raw_html, 'html.parser')
    r = [] 
    for a in html.find_all('a', class_='tab_item'):
        r.append(a['href'])
    return r 

