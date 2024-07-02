from organization import *
from command import Command


class Console:
    @staticmethod
    def start():
        while True:
            # print('Введите команду: ')
            # read_command = input().split()
            read_command = input('Введите команду (help - просмотр всех команд):\n')
            if read_command == 'exit':
                break
            read_parameter = input(f'Введите нужные параметры: <параметр>, <значение>\n'
                                   f'Нажмите Enter, если параметры отсутствуют\n').split(', ')
            # print(read_command)
            # print('/', read_command[1:])
            # if read_command[0] == 'exit':
            #     break
            # Command(read_command[0]).execute(read_command)
            Command(read_command).execute(read_parameter)


