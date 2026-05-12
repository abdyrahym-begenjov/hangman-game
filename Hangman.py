from hangman_image import *
from random import choice
from propython import pyread
from time import sleep
from translator import *

print('en  | ru')
while True:
    lan=input()
    if lan=='en' or lan=='ru':
        break

print(translator('Hangman Game', lan))
print(f'{translator('Creator: Abdyrahym Begenjov', lan)}     (GitHub: abdyrahym-begenjov)')
start=input(translator('Enter to start game: ', lan))
print(translator('Loading...', lan))
sleep(2)

if lan=='ru':
    lst=pyread('russian_words.json')
else:
    lst=pyread('words.json')
point=0

word=choice(lst)
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
        print(translator('You win!!!', lan))
        break    
    w=input(translator('Enter a letter: ', lan))
    if w=='':
        print(translator('You must enter the letter!!!', lan))
        print(translator('Error!!!', lan))
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
            print(translator('This letter is already in the hidden word.', lan))
            print(translator('Error!!!', lan))
            draw(d[point])
            point+=1
        elif point==9:
            draw(d[9])
            print(f'{translator('Game Over!!!', lan)}     {translator('Regular word:', lan)} {word}')
            break
        else:
            print(translator('Error!!!', lan))
            draw(d[point])
            point+=1

end=input(translator('Enter to exit: ', lan))