from organization import *


class Console:
    @staticmethod
    def start(organization):
        while True:
            print('Введите команду: ')
            read_command = input().split()
            # Command(read_command[0]).execute(read_command[1:])
            if read_command == 'exit':
                break
