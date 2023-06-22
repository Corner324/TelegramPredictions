import requests
from bs4 import BeautifulSoup
import lxml
import config

def parsing_horo():
    try:
        response = requests.get(config.url)
        bs = BeautifulSoup(response.text,"lxml")

        temp = bs.find('div', 'article__item article__item_alignment_left article__item_html')

        return temp.text
    except Exception as Ex:
        
        return None