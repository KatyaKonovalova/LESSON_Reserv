import sys

from organization import *


# Надо будет создать по одной переменной в классе Фасада для каждого класса
# Чтобы потом была возможность через эти переменный вызвать нужную функцию класса
# В классе Фасада создать новые методы, в которых по какому-то признаку будут объеденины методы предыдущих классов


class Help:
    # вывести справку по доступным командам
    @staticmethod
    def execute(*args):
        print('Здесь будет справка')


class Info:
    # вывести в стандартный поток вывода информацию о коллекции (тип, дата инициализации, количество элементов и т.д.)
    @staticmethod
    def execute(*args):
        print(f'Дата инициализации: {Organization.initial_date()}\n'
              f'Количество элементов: {len(Organization.objects())}')


class Show:
    # вывести в стандартный поток вывода все элементы коллекции в строковом представлении

    @staticmethod
    def execute(*args):
        for elem in Organization.objects():
            print(elem.name)


class AddElement:
    # добавить новый элемент в коллекцию
    # attributes = ['name', 'description', 'organization']

    # чтобы добавить новый элемент в коллекцию надо создать объект класса Organization

    def new_object(*args):
        new_object = Organization(*args)

    @staticmethod
    def execute(*args):
        pass


class UpdateID:
    # обновить значение элемента коллекции, id которого равен заданному

    pass


class RemoveByID:
    # удалить элемент из коллекции по его id
    # найти элемент по id и удалить его из списка

    @staticmethod
    def execute(*args):
        # print('args[0]', *args[0])
        id = int(*args[0])
        # print('id', id)
        # print('аргумент', *args)
        print(Organization.objects())
        # print('объект', Organization.objects()[id])
        for elem in Organization.objects():
            if elem.id == id:
                Organization.objects().pop(elem.id - 1)
        print(Organization.objects())


class Clear:
    # очистить коллекцию
    @staticmethod
    def execute(*args):
        print(Organization.objects())
        Organization.objects()[:] = []
        print(Organization.objects())


class Save:
    # сохранить коллекцию в файл
    @staticmethod
    def execute(*args):
        with open('elements.txt', 'w') as file:
            file.writelines(f'{elem}\n' for elem in Organization.objects())
            print('Коллекция сохранена в файл "elements.txt"')


class ExecuteScriptFileName:
    # считать и исполнить скрипт из указанного файла.
    # В скрипте содержатся команды в таком же виде, в котором их вводит пользователь в интерактивном режиме.
    # пользователь вводит команды
    # команды сохраняются в файл
    # считываются из файла и выполняются по одной за раз
    pass


class Exit:
    # НЕ УВЕРЕНА ЧТО ЗДЕСЬ НУЖНА ЭТА КОМНАДА, ТАК КАК EXIT ОСУЩЕСТВЛЯЕТСЯ В command.py
    # завершить программу (без сохранения в файл)
    @staticmethod
    def execute(*args):
        sys.exit()

    pass


class Head:
    # вывести первый элемент коллекции
    @staticmethod
    def execute(*args):
        print(Organization.objects()[0])


class RemoveGreater:
    # удалить из коллекции все элементы, превышающие заданный
    # ПРОБЛЕМЫ С parameter, И С ТИПОМ ДАННЫХ ТОЖЕ НЕ ТО
    @staticmethod
    def execute(*args):
        print(*args, type(*args))
        parameter = args[0][0]
        value = int(args[0][1])
        for elem in Organization.objects():
            if isinstance(elem.parameter, str):
                if len(elem.parameter) > value:
                    Organization.objects().remove(elem)
            elif isinstance(elem.parameter, int):
                if elem.parameter > value:
                    Organization.objects().remove(elem)


class History:
    # вывести последние 14 команд (без их аргументов)
    # каждая введенная в консоль команда должна сохраняться в отдельный файл
    pass


class MinByFullName:
    #  вывести любой объект из коллекции, значение поля fullName которого является минимальным
    @staticmethod
    def execute(*args):
        value = len(Organization.objects()[0].full_name)
        # print(value)
        for elem in Organization.objects():
            if len(elem.full_name) < value:
                value = len(elem.full_name)
        print(elem.id)


class PrintFieldDescendingAnnualTurnover:
    # вывести значения поля annualTurnover всех элементов в порядке убывания
    @staticmethod
    def execute(*args):
        an_tur = []
        for elem in Organization.objects():
            an_tur.append(elem.annual_turnover)
        # ПОЧЕМУ НЕ СРАБОТАЛ МЕТОД SORT? ВЫВОДИТ NONE
        result = sorted(an_tur, reverse=True)
        print(result)


class PrintFieldDescendingPostalAddress:
    # вывести значения поля postalAddress всех элементов в порядке убывания
    @staticmethod
    def execute(*args):
        post_address = []
        for elem in Organization.objects():
            address = elem.postal_address.street + ' ' + elem.postal_address.town
            post_address.append(address)
        print(post_address)
        # res = sorted(post_address, reverse=True)
        res = post_address.sort(reverse=True)
        # print(sorted(post_address, reverse=True))
        print(res)
        # ПОПРОБОВАТЬ СДЕЛАТЬ СЛОВАРЬ


class SimpleCommand:
    commands = {'help': Help,
                'info': Info,
                'show': Show,
                'clear': Clear,
                'save': Save,
                'exit': Exit,
                'head': Head,
                'min': MinByFullName,
                'print annual turnover': PrintFieldDescendingAnnualTurnover,
                'print postal address': PrintFieldDescendingPostalAddress, }

    def __init__(self, name):
        # print('3', name)
        self.command = SimpleCommand.commands[name]

    def execute(self):
        self.command.execute()


class CompositeCommand:
    commands = {'add': AddElement,
                'remove by id': RemoveByID,
                'remove greater': RemoveGreater, }

    def __init__(self, name):
        # print('4', name)
        self.command = CompositeCommand.commands[name]

    def execute(self, *args):
        # print('передача', *args)
        self.command.execute(*args)


class Command:
    def __init__(self, name):
        self.name = name
        # print('5', self.name)
        if self.name in CompositeCommand.commands:
            self.__command = CompositeCommand
        else:
            self.__command = SimpleCommand

    def execute(self, *args):
        # print(*args)
        # print('*', *args)
        # print('args[0]', args[0][0])
        if args[0] == ['']:
            self.__command(self.name).execute()
        else:
            self.__command(self.name).execute(*args)
