today = list() # today = []
tomorrow = list() # tomorrow = []
other = list() # other = []

HELP = '''
Список доступных команд:
* print  - напечать все задачи на заданную дату
* todo - добавить задачу
* help - Напечатать help
'''

while True:
    command = input('Введите команду: ')
    if command == 'help':
        print(HELP)
    elif command == 'todo':
        date = input('Введите дату: ')
        task = input('Введите задачу: ')
        if date == 'Сегодня': 
          today.append(task)
        elif date == 'Завтра':
          tomorrow.append(task)
        else:
          other.append(task)
        print(f'Задача {task} добавлена')
    elif command == 'print':
        print('Сегодня')
        for task in today:
          print(task)
        print('Завтра')
        for task in tomorrow:
          print(task)
        print('Другие')
        for task in other:
          print(task)
    elif command == 'exit':
        print('Спасибо за использование! До свидания!')
        break
    else:
        print('Неизвестная команда!')
        break
