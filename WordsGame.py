import re
import codecs
import copy
from math import inf


def set_el(string: str, ind: int, el: str):
    new_string = ''
    for i in range(len(string)):
        if i == ind:
            new_string += el
        else:
            new_string += string[i]
    return new_string



words = dict()
alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэяю'

with codecs.open('dictionary.txt', encoding='utf-8') as fin:
    text = fin.read()

words_vsp = text.split('\n')
for word in words_vsp:
    word = re.sub(r'\r', '', word)
    if not(word[-1] == 'ы' or word[-1] == 'и') and len(word) <= 6:
        words[word] = False



def change(dct__: dict, path__: list, last_let_ind: int, max_depth: int, start_word: str, end_word: str):
    if len(path__) > max_depth:
        return [-1]
    dct = dct__
    path = copy.deepcopy(path__)
    path.append(start_word)
    dct[start_word] = True
    if start_word == end_word:
        return path

    for i in range(len(start_word)):
        if i == last_let_ind:
            continue
        for let in alph:
            new_word = set_el(start_word, i, let)
            if new_word in dct.keys():
                if dct[new_word] is False:
                    res = change(dct, path, i, max_depth, new_word, end_word)
                    if res[-1] == end_word:
                        return res

    return [-1]


def short_change(start_word: str, end_word: str):
    if change(copy.deepcopy(words), [], -1, len(words), start_word, end_word)[0] != -1:
        results = []
        for max_depth in range(len(words)):
            res = change(copy.deepcopy(words), [], -1, max_depth, start_word, end_word)
            if res[0] != -1:
                return res



# path1 = short_change('волк', 'коза')
# print(path1)

print('Введите 1 слово')
word1 = input()
print('Введите 2 слово')
word2 = input()


print(short_change(word1, word2))





