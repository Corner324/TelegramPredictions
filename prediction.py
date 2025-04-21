import requests
from bs4 import BeautifulSoup
import lxml
import config


def parsing_horo():
    try:
        response = requests.get(config.url)
        bs = BeautifulSoup(response.text, "lxml")

        temp = bs.find(
            "main", "e45a4c1552 be13d659a4 navigationContainer_1 dcced6f448"
        )

        return temp.text
    except Exception as e:
        print(e)

if __name__ == "__main__":
    print(parsing_horo())