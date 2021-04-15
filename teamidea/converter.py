# -*- coding: cp1251 -*-
# Разработать программу, которая выводит курс японских иен к российскому рублю,
# на основании данных, запрошенных с сайта
# http://www.cbr.ru/scripts/XML_daily.asp */

import requests, re
import xml.etree.ElementTree as ET



url = 'http://www.cbr.ru/scripts/XML_daily.asp'
response = requests.get(url)
xml = response.content
root = ET.fromstring(xml)
print(root[33][2].text, root[33][3].text, '-', root[33][4].text + ' рубля')
