import os
import re

import requests
from bs4 import BeautifulSoup  # pip install beautifulsoup4
from tqdm import tqdm

def download_google(word):
    # url = 'https://www.google.com/search?q=' + word + '&client=opera&hs=cTQ&source=lnms&tbm=isch&sa=X&ved=0ahUKEwig3LOx4PzKAhWGFywKHZyZAAgQ_AUIBygB&biw=1920&bih=982'
    url = 'https://www.bing.com/images/search?q=' + word
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    links = soup.find_all('a', {'class': 'thumb'})

    for link in links:
        link = link.get('href')
        s = "curl -s -L -o '%s' '%s'" % (link.split('/')[-1], link)
        os.system(s)

def download_image(word):
    url = ''
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    links = soup.find_all('a', {'class': 'thumb'})

    for link in links:
        link = link.get('href')
        s = "curl -s -L -o '%s' '%s'" % (link.split('/')[-1], link)
        os.system(s)


if __name__ == '__main__':
    # word = input("Input key word: ")
    # download_baidu(word)
    download_image('honeybees')
