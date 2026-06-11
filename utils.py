from translator import *
from propython import *
from subprocess import run
from platform import system
from hangman_image import *

def clear_screen():
    current_os=system()
    if current_os=='Windows':
        run(["cls"], shell=True)
    else:
        run(['clear'])

def enter_lang(data):
    print('English |  Русский')
    while True:
        chosen_language=input()
        chosen_language=chosen_language.title().strip()
        match chosen_language:
            case 'Русский':
                lang='ru'
                words_list=pyread('russian_words.json')
                break
            case 'English':
                lang='en'
                words_list=pyread('words.json')
                break
            case _:
                continue
    
    data['language']=lang
    data['words']=words_list
    pywrite('data.json', data)
    return lang, words_list

def enter_name(lang, data):
    while True:
        name=input(translator('Enter your name: ', lang))
        if name!='':
            data['name']=name
            pywrite('data.json', data)
            return name
        
def new_word(word, lang):
    word=word.strip().title()
    if lang=='ru':
        word=translator(word, 'en1')
    return word

def mistake_was_maden(d, point, lang):
    print(translator('Error!!!', lang))
    draw(d[point])
    point+=1
    return point

def draw_leaderboard(base, lang):
    print(translator('LEADERBOARD:', lang))
    base=list(base.items())
    base.sort(key=lambda x: x[1][0]-x[1][1], reverse=True)
    base=dict(base)

    lst=['VICTORIES', 'DEFEATS', 'OVERALL RESULT']
    lst=[f'{translator(i, lang):<16}|' for i in lst]
    lst=' '.join(lst)
    line1=f'|{translator('NAME |', lang):>18} {lst:<16}'
    line='-'*len(line1)
    print(line)
    print(line1)
    print(line)

    for i, j in base.items():
        name=i
        a=str(j[0])
        b=str(j[1])
        c=j[0]-j[1]
        name1=f'{name} |'
    
        line2=f'|{name1:>18} {a:<16}| {b:<16}| {c:<16}|'
        print(line2)
        print(line)