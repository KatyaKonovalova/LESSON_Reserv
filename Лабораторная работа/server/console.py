from organization import *
from command import Command


class Console:
    @staticmethod
    def start():
        while True:
            print('Введите команду: ')
            read_command = input().split()
            if read_command[0] == 'exit':
                break
            Command(read_command[0]).execute(*read_command[1:])
