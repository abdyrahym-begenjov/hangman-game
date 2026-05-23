from hangman_image import *
from random import choice
from propython import pyread, pywrite
from time import sleep
from translator import *
from subprocess import run
from platform import system

base=pyread('base.json')
data=pyread('data.json')

def clear_screen():
    current_os=system()
    if current_os=='Windows':
        run(["cls"], shell=True)
    else:
        run(['clear'])

def enter_name():
    while True:
        name=input(translator('Enter your name: ', lang))
        if name!='':
            data['name']=name
            pywrite('data.json', data)
            return name

def enter_lang():
    print('English |  Русский')
    while True:
        chosen_language=input()
        chosen_language=chosen_language.title().strip()
        if chosen_language=='English' or chosen_language=='Русский':
            break

    match chosen_language:
        case 'Русский':
            lang='ru'
            words_list=pyread('russian_words.json')
        case 'English':
            lang='en'
            words_list=pyread('words.json')
    data['language']=lang
    data['words']=words_list
    pywrite('data.json', data)
    return lang, words_list

name=data['name']
lang=data['language']
words_list=data['words']

if lang=='' and words_list==[]:
    lang, words_list=enter_lang()

if name=='':
    name=enter_name()

if name not in base:
    base[name]={'Victories': 0, 'Defeats': 0}

while True:
    print(translator('Hangman Game', lang))
    print(f'{translator('Creator: Abdyrahym Begenjov', lang)}     (GitHub: abdyrahym-begenjov)')
    print(translator('Game      Rules      Highscores      Settings      Exit', lang))
    mode=input(translator('Choose a game mode: ', lang))
    mode=mode.title().strip()
    if lang=='ru':
        mode=translator(mode, 'en1')
    match mode:
        case 'Game':
            start=input(translator('Enter to start game: ', lang))
            print(translator('Loading...', lang))
            sleep(2)

            point=0 

            word=choice(words_list)
            word=word.lower()
            task='_ '*len(word)
            task1=task.split()
            print(task)

            lst=[]
            result={i: j for i, j in enumerate(word)}
            result1={}
            for i, j in result.items():
                result1.setdefault(j, []).append(i)

            while True:
                if '_' not in task1:
                    print(word)
                    print(translator('You win!!!', lang))
                    base[name]['Victories']+=1
                    break    
                w=input(translator('Enter a letter: ', lang))
                if w=='':
                    print(translator('You must enter the letter!!!', lang))
                    print(translator('Error!!!', lang))
                    draw(d[point])
                    point+=1
                else:
                    w=w.lower().strip()
                    if w in word and w not in lst:
                        lst.append(w)
                        num=len(result1[w])
                        for n in range(num):
                            i=result1[w][n]
                            task1[i]=w
                        task=' '.join(task1)
                        print(task)
                    elif w in lst:
                        print(translator('This letter is already in the hidden word.', lang))
                        print(translator('Error!!!', lang))
                        draw(d[point])
                        point+=1
                    elif point==9:
                        draw(d[9])
                        print(f'{translator('Game Over!!!', lang)}     {translator('Regular word:', lang)} {word}')
                        base[name]['Defeats']+=1
                        break
                    else:
                        print(translator('Error!!!', lang))
                        draw(d[point])
                        point+=1
            pywrite('base.json', base)
            end=input(translator('Enter to exit: ', lang))
            clear_screen()
        
        case 'Rules':
            if lang=='ru':
                rules=pyread('ru_rules.txt')
            else:
                rules=pyread('en_rules.txt')
            print(rules)
            end=input(translator('Enter to exit mode: ', lang))
            clear_screen()
        
        case 'Highscores':
            line1=base[name]['Victories']
            line2=base[name]['Defeats']
            print(f'{translator('VICTORIES', lang)}: {line1}')
            print(f'{translator('DEFEATS', lang)}: {line2}')
            end=input(translator('Enter to exit: ', lang))
            clear_screen()

        case 'Settings':
            while True:
                print(f'{translator('Name', lang)}: {data['name']}')
                print(f'{translator('Language', lang)}: {data['language']}')
                change=input(translator('Do you want to change parameters (Enter \"Name\" or \"Language\"): ', lang))
                change=change.title().strip()
                if lang=='ru':
                    change=translator(change, 'en1')
                match change:
                    case 'Name':
                        name=enter_name()
                        if name not in base:
                            base[name]={'Victories': 0, 'Defeats': 0}
                        clear_screen()
                    case 'Language':
                        lang, words_list=enter_lang()
                        clear_screen()
                    case _:
                        break
            clear_screen()

        case 'Exit':
            exit_confirm=input(translator('Do you want to exit (\"Yes\" or \"No\"): ', lang))
            exit_confirm=exit_confirm.title().strip()
            if lang=='ru':
                exit_confirm=translator(exit_confirm, 'en1')
            if exit_confirm=='No':
                clear_screen()
            else:
                print(translator('Goodbye!!!', lang))
                input(translator('Enter to exit: ', lang))
                break
        case _:
            clear_screen()