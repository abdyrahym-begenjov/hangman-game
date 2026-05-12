rutranslate={
    'Enter the word: ': 'Введите слово: ',
    'Error!!!': 'Ошибка!!!',
    'Game Over!!!': 'Игра окончена!!!',
    'You win!!!': 'Вы победили!!!',
    'Regular word:': 'Правильное слово:',
    'Enter a letter: ': 'Введите букву: ',
    'Hangman Game': 'Виселица',
    'Creator: Abdyrahym Begenjov': 'Создатель: Абдырахым Бегенджов',
    'Enter to start game: ': 'Нажмите, чтобы начать игру: ',
    'Loading...': 'Загрузка...',
    'This letter is already in the hidden word.': 'Эта буква уже есть в загаданном слове.',
    'You must enter the letter!!!': '',
    'Enter to exit: ': 'Введите для выхода: '
             }


entranslate={j: i for i, j in rutranslate.items()}


def translator(word, language):
    match language:
        case 'en':
            return word
        case 'en1':
            if word not in entranslate:
                return 'Error!!!'
            return entranslate[word]
        case 'ru':
            return rutranslate[word]
        case _:
            return '???'