from organization import *
from command import Command


class Console:
    @staticmethod
    def start():
        while True:
            print('Введите команду: ')
            read_command = input().split()
            # print(read_command)
            # print('/', read_command[1:])
            if read_command[0] == 'exit':
                break
            Command(read_command[0]).execute(read_command)
