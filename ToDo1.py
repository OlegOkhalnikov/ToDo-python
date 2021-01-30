HELP = """

help - напечатать справку
add - добавить задачу в список
print - напечать все задачи из списка
exit - выход

"""
tasks = ['Убраться дома']

print(HELP)

while True:
  command = input('Введите команду: ')
  command = command.strip().lower()
  if command == 'help':
    print(HELP)
  elif command =='add':
    task = input('Введите задачу: ')
    tasks.append(task)
  elif command == 'print':
    print(tasks)
  elif command == 'exit':
    print('Спасибо за использование! До свидания!')
    break
  else:
    print('Неизвестная команда')
    break