# hangman-game
Hangman Game
# Hangman Game (Виселица)
## English
A simple Python console implementation of the classic Hangman game. The player must guess the hidden word letter by letter before the "hangman" is fully drawn.
### ⚙️ Features
* **Random word selection:** The program loads a list of words from an external JSON file.
* **Dynamic display:** The word state is updated in real time after each guessed character.
* **Visualization:** Drawing the hangman stages when mistakes are made.
* **Repetition logic:** Handling multiple occurrences of the same letter in a word.
### 🛠 Tech stack
* **Python 3.x**
* Random module for word selection.
* Propython library (pyread function) for data parsing.  * Custom hangman_image module for graphical support in the console.
### 🚀 How to run
1. Make sure you have installed the hangman_image.py and words.json files in the project's root directory.
2. Run the main script:
python Hangman.py
3. Enter a letter when prompted to Enter a letter: .
### 📝 Game Rules
* You have **10 tries** (0 to 9) before the game ends in defeat.
* If you guess a letter correctly, it is revealed in a word, and the error counter is not incremented.
* The game ends in victory if all the letters are guessed correctly.
## Русский
Простая консольная реализация классической игры **"Виселица"** на языке Python. Игрок должен угадать загаданное слово по буквам, прежде чем "палач" будет полностью нарисован.
### ⚙️ Функционал
 * **Случайный выбор слов:** Программа загружает список слов из внешнего JSON-файла.
 * **Динамическое отображение:** Состояние слова обновляется в реальном времени после каждого угаданного символа.
 * **Визуализация:** Отрисовка этапов "виселицы" при совершении ошибок.
 * **Логика повторов:** Обработка нескольких вхождений одной и той же буквы в слове.
### 🛠 Технологический стек
 * **Python 3.x**
 * Модуль random для выбора слов.
 * Библиотека propython (функция pyread) для парсинга данных.
 * Пользовательский модуль hangman_image для графического сопровождения в консоли.
### 🚀 Как запустить
 1. Убедитесь, что у вас установлены файлы hangman_image.py и words.json в корневой директории проекта.
 2. Запустите основной скрипт:
   python Hangman.py
 3. Введите букву, когда появится запрос Enter a letter: .
### 📝 Правила игры
 * У вас есть **10 попыток** (от 0 до 9), прежде чем игра завершится поражением.
 * Если вы угадываете букву, она открывается в слове, а счетчик ошибок не увеличивается.
 * Игра заканчивается победой, если все буквы разгаданы.
