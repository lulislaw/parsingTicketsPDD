import os
import requests
from bs4 import BeautifulSoup
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM


# Парсинг знаков с дрома
url = 'https://www.drom.ru/pdd/pdd/signs/'
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

imgs = soup.find_all('div', attrs={'class': 'pub__img'})
i = 0
for img in imgs:
    i=i+1
    img_url = img.find('img')['src']
    path = "imgs"
    pathPng = "imgspng"
    if not os.path.exists(path):
        os.makedirs(path)
    img_filename = os.path.join(path, f'image{i}.svg')
    img_filenamepng = os.path.join(pathPng, f'image{i}.png')
    with open(img_filename, 'wb') as f:
        f.write(requests.get(img_url).content)
    drawing = svg2rlg(img_filename)
    renderPM.drawToFile(drawing, img_filenamepng, fmt='PNG')