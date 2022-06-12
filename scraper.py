import re
import urllib.requests from bs4
import BeautifulSoup
import requests from google.colab
import files

img = []
for i in range(1, 2):
    for j in range(1, 200):
        URL = 'http://www.mangapanda.com/onepunch-man/{}/{}'.format(i, j)
        request = requests.get(URL)
        if request.status_code == 200:
            page = requests.get(URL)
            page_content = BeautifulSoup(page.content, 'html.parser')
            row_data = []
            for row in page_content.findAll('script', attrs={'type': 'text/javascript'}):
                row_data.append(row.text)
            img.append(re.findall('[^.]ttps. *jpg', row_data[2]))
        else:
            break
