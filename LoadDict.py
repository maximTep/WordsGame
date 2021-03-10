import requests
from bs4 import BeautifulSoup
import re


def load_dict():
    let = 'А'
    website_url = requests.get('https://ru.wiktionary.org/'
                               'wiki/%D0%98%D0%BD%D0%B4%D0%B5%D0%BA%D1%81:%'
                               'D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9_%D1%8F%D0%B7%D1%8B%D0%BA/' + let).text
    soup = BeautifulSoup(website_url, 'lxml')
    # print(soup.prettify())


    words = []

    table_find = soup.find('div', {'class': 'index'})
    words_construct_find = table_find.find_all('li')
    for words_construct in words_construct_find:
        word = str(words_construct.find('a').get('title'))
        print(word)
        if word == re.search(r'\w+', word).group(0):
            words.append(word)

    f = open('dictionary.txt', 'w')
    for word in words:
        f.write(word + '\n')
    f.close()


