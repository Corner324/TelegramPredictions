import requests
from bs4 import BeautifulSoup
import lxml

def parsing_horo():
    url = 'https://horo.mail.ru/prediction/aries/today/'
    response = requests.get(url)
    bs = BeautifulSoup(response.text,"lxml")

    temp = bs.find('div', 'article__item article__item_alignment_left article__item_html')

    return temp.text