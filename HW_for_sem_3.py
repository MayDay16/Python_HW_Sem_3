homework = True
while homework:
    homework = (input("Введите номер задачи (1, 2, 3), для выхода введите 'exit': "))
    if homework == 'exit':
        homework = not homework
    elif homework == '1':
        fibonacci()
    elif homework == '2':
        fruit_search()
    elif homework == '3':
        bot_chat()

# Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8

def fibonacci ():
    N1 = 1
    N2 = 1
    count = int(input("Введите число первых элементов последовательности Фибоначчи: "))
    data = open('fibonacci.txt', 'w')
    for i in range(count):
        data.writelines(str(N1) + '\n')
        (N1, N2) = (N2, N1 + N2)
    print('Файл "fibonacci.txt" создан/перезаписан')
    data.close()
fibonacci ()

# Задача 2. В файле находятся названия фруктов. 
# Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.

def fruit_search():
    path = 'fruit_list.txt'
    data = open(path, "r", encoding='utf-8')
    text = data.readlines()
    data.close()

    symbol = input("Введите букву: ").upper()
    print(f'Фрукты на букву "{symbol}" это:')
    for line in text:
        if line[0] == symbol:
            print(line)
        else:
            pass
fruit_search()


# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут».
# Если фраза ему неизвестна, он выводит соответствующую фразу.
# «как тебя зовут?» –> меня зовут Анатолий

dict = \
    {
        'Привет': 'И тебе привет',
        'Здравствуй': 'И тебе не болеть',
        'Как тебя зовут?': 'Моё им Легион!',
        'Ты кто?': 'Твой бот!',
        'Ты кто по жизни?': 'Бот, как и ты!',
        'Как жизнь?': 'Неплохо. Как сам?',
        'Как дела?': 'Отлично!',
        'Пока!': 'До свидания!',
        'До свидания!': 'Пока!',
        'Выход': 'Ты заходи, если что.'
    }

def bot_chat():
    key = ""
    while key != "Выход":
        key = str(input("Пользователь: "))
        if key in dict:
            print(f"Бот: {dict[key]}")
        else:
            print("Не могу вас понять, повторите пожалуйста еще раз.")

bot_chat()

