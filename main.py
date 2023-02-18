import os
import requests
import json
from bs4 import BeautifulSoup

#Парсинг билетов ПДД с drom.ru
url = 'https://www.drom.ru/pdd/bilet_'

for i in range(1, 41):
    urlBilet = url + i.__str__()
    response = requests.get(urlBilet)
    soup = BeautifulSoup(response.content, "html.parser")
    contentBox = soup.find_all('div', attrs={'class': 'pdd-ticket b-media-cont'})
    for bo in range(len(contentBox)):
        numberQuest = contentBox[bo].find('a', attrs={'class': 'b-link'})
        quest = contentBox[bo].find('div', attrs={'class': 'b-title b-title_type_h4 b-title_no-margin'})
        answers = contentBox[bo].find_all('div', attrs={
            'class': 'b-flex b-flex_align_left b-random-group b-random-group_margin_r-size-s bm-forceFlex'})
        numQuest = numberQuest.text.strip()
        textQuest = quest.text.strip()
        finalB = bo + 1
        # print('Правильный ответ')
        succesAns = soup.find('div', attrs={'id': f'a{finalB}'}).text.strip()
        # print('Варианты ответов')
        # img = contentBox[bo].find('img', attrs={'class': 'b-image b-image__image'})
        list = []
        # if(img != None):
        #     img_url = img['src']
        #     path = "imgs" + i.__str__() + "bilet"
        #     if not os.path.exists(path):
        #         os.makedirs(path)
        #     img_filename = os.path.join(path, f'image{bo+1}.jpg')
        #     with open(img_filename, 'wb') as f:
        #         f.write(requests.get(img_url).content)
        for ans in answers:
            tempStr = ans.text.strip().replace('\n', ' ')
            tempStr = tempStr.replace('                          ', ' ')
            list.append(tempStr)
        while (list.__len__() != 5):
            list.append('')
        value = {
            "nubmerQuest": numQuest,
            "textQuest": textQuest,
            "sucAns": succesAns,
            "ans1": list[0],
            "ans2": list[1],
            "ans3": list[2],
            "ans4": list[3],
            "ans5": list[4]
        }
        save_file = open(f'bilet{i}quest{bo + 1}.json', "w", encoding="utf-8")
        json.dump(value, save_file, indent=6, ensure_ascii=False)
        save_file.close()


