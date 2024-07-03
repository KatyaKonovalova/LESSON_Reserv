import sys

from organization import *


# Надо будет создать по одной переменной в классе Фасада для каждого класса
# Чтобы потом была возможность через эти переменный вызвать нужную функцию класса
# В классе Фасада создать новые методы, в которых по какому-то признаку будут объеденины методы предыдущих классов


class Help:
    # вывести справку по доступным командам
    @staticmethod
    def execute(*args):
        with open('help_doc.txt', 'r', encoding='utf-8') as file:
            print(file.read())


class Info:
    # вывести в стандартный поток вывода информацию о коллекции (тип, дата инициализации, количество элементов и т.д.)
    @staticmethod
    def execute(*args):
        print(f'Дата инициализации: {Organization.initial_date()}\n'
              f'Количество элементов: {len(Organization.objects())}')


class ShowSaveFile:
    # вывести в стандартный поток вывода все элементы коллекции в строковом представлении

    @staticmethod
    def execute(*args):
        # Почему с encoding='utf-8' вылезает ошибка?
        with open('elements.txt', 'r', encoding='utf-8') as file:
            print(file.read())


class ShowCollection:
    # вывести в стандартный поток вывода все элементы коллекции в строковом представлении
    # ПРОДУМАТЬ МОМЕНТ С СОХРАНЕНИЕМ

    @staticmethod
    def execute(*args):
        for elem in Organization.objects():
            print(elem)


class AddElement(Organization):
    # добавить новый элемент в коллекцию
    def __init__(self, *args):
        super().__init__(*args)
        print(args)

    # чтобы добавить новый элемент в коллекцию надо создать объект класса Organization

    @staticmethod
    def execute(*args):
        new_object = Organization(*args)
        print(new_object)
        print(new_object.name)


# '5', 'Фабрика', 70, 5.5, Address('Волковская', 'Саратов')
# 5, Фабрика, 70, 5.5, Address('Волковская', 'Саратов')

class UpdateID:
    # обновить значение элемента коллекции, id которого равен заданному
    # надо передавать параметр, значение которого хотим изменить и номер id
    # что делать с параметрами, у которых внутри несколько значений, вроде адреса и координат?
    @staticmethod
    def execute(*args):
        id = int(*args[0][2])
        print(Organization.objects())
        # print('объект', Organization.objects()[id])
        print(args[0][0])
        parameter = args[0][0]
        value = args[0][1]
        for elem in Organization.objects():
            if elem.id == id:
                old_elem = getattr(elem, parameter)
                print(old_elem)
                setattr(elem, parameter, value)
                new_el = getattr(elem, parameter)
                print(new_el)


# getattr(object, name, default)


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
        with open('elements.txt', 'w', encoding='utf-8') as file:
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
            use_elem = getattr(elem, parameter)
            if isinstance(use_elem, str):
                if len(use_elem) > value:
                    Organization.objects().remove(elem)
            elif isinstance(use_elem, int or float):
                if use_elem > value:
                    Organization.objects().remove(elem)


class History:
    # вывести последние 14 команд (без их аргументов)

    @staticmethod
    def execute(*args):
        with open('history.txt', 'r', encoding='utf-8') as file:
            print(file.read()[-1:])


class MinByFullName:
    #  вывести любой объект из коллекции, значение поля fullName которого является минимальным
    # НЕ ПОНИМАЮ КАК РАБОТАЕТ
    @staticmethod
    def execute(*args):
        print(min(Organization.objects(), key=lambda x: len(x.full_name)))


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
                'show collection': ShowCollection,
                'show file': ShowSaveFile,
                'clear': Clear,
                'save': Save,
                'exit': Exit,
                'head': Head,
                'history': History,
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
                'update id': UpdateID,
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

    @staticmethod
    def save_command(command):
        with open('history.txt', 'a', encoding='utf-8') as file:
            file.write(f'{command}\n')

    def execute(self, *args):
        # print(*args)
        # print('*', *args)
        # print('args[0]', args[0])
        if args[0] == ['']:
            self.__command(self.name).execute()
        else:
            self.__command(self.name).execute(*args)
