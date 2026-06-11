from hangman_image import *
from random import choice
from propython import pyread, pywrite
from time import sleep
from translator import *
from utils import *

while True:
    base=pyread('base.json')
    data=pyread('data.json')

    name=data['name']
    lang=data['language']
    words_list=data['words']

    if lang=='' and words_list==[]:
        lang, words_list=enter_lang(data)
        clear_screen()

    if name=='':
        name=enter_name(lang, data)
        clear_screen()

    if name not in base:
        base[name]=[0, 0]
    
    print(translator('Hangman Game', lang))
    print(f'{translator('Creator: Abdyrahym Begenjov', lang)}     (GitHub: abdyrahym-begenjov)')
    print(translator('Game      Rules      Highscores      Settings      Exit', lang))
    mode=input(translator('Choose a game mode: ', lang))
    mode=new_word(mode, lang)
    clear_screen()
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
                    base[name][0]+=1
                    break    
                w=input(translator('Enter a letter: ', lang))
                if w=='':
                    print(translator('You must enter the letter!!!', lang))
                    point=mistake_was_maden(d, point, lang)
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
                        point=mistake_was_maden(d, point, lang)
                    elif point==9:
                        draw(d[9])
                        print(f'{translator('Game Over!!!', lang)}     {translator('Regular word:', lang)} {word}')
                        base[name][1]+=1
                        break
                    else:
                        point=mistake_was_maden(d, point, lang)
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
            draw_leaderboard(base, lang)
            end=input(translator('Enter to exit: ', lang))
            clear_screen()

        case 'Settings':
            while True:
                print(f'{translator('Name', lang)}: {data['name']}')
                print(f'{translator('Language', lang)}: {data['language']}')
                change=input(translator('Do you want to change parameters (Enter \"Name\" or \"Language\"): ', lang))
                change=new_word(change, lang)
                match change:
                    case 'Name':
                        name=enter_name(lang, data)
                        if name not in base:
                            base[name]={'Victories': 0, 'Defeats': 0}
                        clear_screen()
                    case 'Language':
                        lang, words_list=enter_lang(data)
                        clear_screen()
                    case _:
                        break
            clear_screen()

        case 'Exit':
            exit_confirm=input(translator('Do you want to exit (\"Yes\" or \"No\"): ', lang))
            exit_confirm=new_word(exit_confirm, lang)
            if exit_confirm=='No':
                clear_screen()
            else:
                print(translator('Goodbye!!!', lang))
                input(translator('Enter to exit: ', lang))
                break
        case _:
            clear_screen()