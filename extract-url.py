# this prompt was designed for websites' html codes that signal a url using <a href=link>
# adjust to other tags if the code doesn't use <a>

import requests
import re
from bs4 import BeautifulSoup

r = requests.get('link')

linkRegex = re.compile(r'^https?')

soup = BeautifulSoup(r.content, 'html.parser')

list = []
for i in soup.find_all('a'):
    list.append(i.get('href'))

# 1: extract all urls available in the html code
for i in list:
    try:
        if linkRegex.search(i) != None:
            print(i)
        else:
            pass
    except TypeError:
        print(i)

# 2: access url and return only when its status code is 200 (ready to use) -> still modifying
for i in list:
    try:
        if linkRegex.search(i) != None and requests.get(i).status_code == 200:
            print(i)
        else:
            pass
    except TypeError:
        print(i)
