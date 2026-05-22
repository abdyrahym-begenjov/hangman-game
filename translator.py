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
    'You must enter the letter!!!': 'Вы должны ввести букву!!!',
    'Enter to exit: ': 'Введите для выхода: ',
    'Enter your name: ': 'Введите свое имя: ',
    'Enter to exit mode: ': 'Войдите в режим выхода: ',
    'Game      Highscores      Settings      Exit': 'Игра      Рекорды      Настройки      Выход',
    'Choose a game mode: ': 'Выберите режим игры: ',
    'Do you want to change parameters (Enter \"Name\" or \"Language\"): ': 'Хотите ли вы изменить параметры (введите \"Имя\" или \"Язык\"): ',
    'Do you want to exit (\"Yes\" or \"No\"): ': 'Вы хотите завершить (\"Да\" или \"Нет\"): ',
    'Goodbye!!!': 'До свидания!!',
    'Name': 'Имя',
    'Language': 'Язык',
    'Return': 'Вернуться',
    'Game': 'Игра',
    'Rules': 'Правилы',
    'Records': 'Рекорды',
    'Settings': 'Настройки',
    'Exit': 'Выход',
    'VICTORIES': 'ПОБЕДЫ',
    'DEFEATS': 'ПОРАЖЕНИЯ'
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