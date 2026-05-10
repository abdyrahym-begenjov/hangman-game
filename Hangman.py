from hangman_image import *
from random import choice
from propython import pyread

lst=pyread('words.json')
point=0
word=choice(lst)
word=word.lower()
task='_ '*len(word)
task1=task.split()
print(task)
result={i: j for i, j in enumerate(word)}
result1={}
for i, j in result.items():
    result1.setdefault(j, []).append(i)
while True:
    if '_' not in task1:
        print(word)
        print('You win!!!')
        break    
    w=input('Enter a letter: ')
    if w in word:
        num=len(result1[w])
        for n in range(num):
            i=result1[w][n]
            task1[i]=w
        task=' '.join(task1)
        print(task)
    elif point==9:
        draw(d[9])
        print(f'Game Over!!!     Regular word: {word}')
        break
    else:
        print('Error!!!')
        draw(d[point])
        point+=1