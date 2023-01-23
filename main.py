# 1. Приветствие
# 2. Объяснение правил игры
# 3. Создание русско-английского словаря
# 4. Описание алгоритма сбора слов:
# 4.1. Выбор 4-х случайных слов
# 4.2. Выбор 1 слова, которое будет вопросом
# 4.3. Задать вопрос игроку
# 4.4. Вывод на экран вариантов ответа
# 5. Получение ответа от игрока
# 6. Сравнение ответов и выдача ответа машины

import random

# приветствие
print('Приветствую тебя в этой игре, будущий полиглот!')

# объяснение правил
print("Вам будет дано слово на русском языке, также будет выдано 4 варианта ответа на английском. Выберите самый подходящий правильный ответ на ваш взгляд!")

EN_RU_VOCABULARY = {
  'fortitude' : 'выносливость',
  'henchman' : 'приспешник',
  'impasse' : 'тупик',
  'brigand' : 'разбойник',
  'confound it' : 'чёрт бы его побрал',
  'perpetuity' : 'вечность',
  'convoke' : 'созывать',
  'equanimity' : 'невозмутимоть',
  'connive' : 'потворствовать',
  'sliver' : 'щепка',
  'in a pinch' : 'в крайнем случае',
  'licorice' : 'лакрица'
}

# создаём инверсированный словарь
for item in EN_RU_VOCABULARY:
  print(item.)

# выбираем 4 случайных слова
random_words = random.sample(VOCABULARY.keys(), 4) 

# выбираем слово, которое будет вопросом
random_word = random.choice(random_words)

# задаём вопрос игроку
print(f"Переведите слово '{random_word}' на аглийский язык")

# выводим на экран варианты ответа
for index, word in enumerate(random_words): 
  # word = random_words[0], index = 0 ...
  print(f"{index + 1}. {VOCABULARY[word]}")

# получаем ответ от игрока
player_answer = input("Введите ваш ответ в виде числа от 1 до 4: ")

# Защита от выхода за пределами списка random_words 
answer_is_correct = False
while (not answer_is_correct):
  if player_answer.isdigit():
    player_answer = int(player_answer)
    if (player_answer > 4 or player_answer < 1):
      player_answer = input('Введите число от 1 до 4: ')
    else:
      answer_is_correct = True
  else:
    player_answer = input('Введите число от 1 до 4: ')

# проверяем полученный ответ
if random_words[player_answer - 1] == random_word:
  print("Верно!")
else:
  print(f"Неверно! Правильный ответ: {VOCABULARY[random_word]}")