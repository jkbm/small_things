#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs
import json

url = "https://www.olx.ua/nedvizhimost/kvartiry-komnaty/arenda-kvartir-komnat/kvartira/kiev/?search%5Bfilter_float_price%3Afrom%5D=7000&search%5Bfilter_float_price%3Ato%5D=8000&search%5Bfilter_float_number_of_rooms%3Afrom%5D=2&search%5Bfilter_float_number_of_rooms%3Ato%5D=2&search%5Bphotos%5D=1"

r = requests.get(url)

soup = bs(r.content, "html.parser")
offers = soup.find_all('td', class_="offer")

with open('appartments.json', 'r') as base:
    jbase = json.load(base)
    base.close()

links = [x['link'] for x in jbase['offers']]
districts = set()
today_count = 0
for offer in offers:
    try:
        title = offer.find('a', class_='link').find('strong').get_text()
        price = offer.find('p', class_='price').get_text()
        link = offer.find('a', class_='link', href=True)['href']
        bottom = offer.find('td', class_="bottom-cell")
        time = bottom.find_all('span')[-1].get_text()

        if "Сегодня" in time:
            print(title)
            print("{0} Ссылка: {1}".format(price.strip(), link.strip()))
            bottom_clean = "|".join([s.get_text().strip() for s in bottom.find_all('span')])
            print(bottom_clean + "\n")
            today_count += 1
            districts.add(bottom.find_all('span')[0].get_text().strip())
            if link not in links:
                d_offer = {'title': title, 'price': price, 'link': link, 'bottom': bottom_clean}
                jbase['offers'].append(d_offer)

    except Exception as e:
        print("Error in html: %s" % e)

with open('appartments.json', 'w+') as base:
    jstr = json.dumps(jbase)
    base.write(jstr)
    base.close()
print("\nНайдено {0} предложений в таких районах: {1}".format(today_count, "; ".join(districts)))
