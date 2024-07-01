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
    # по id достать найти элемент и изменить значение характеристики
    pass


class RemoveByID:
    # удалить элемент из коллекции по его id
    # найти элемент по id и удалить его из списка

    def __init__(self, *args):
        self.id = id

    @staticmethod
    def execute(*args):
        print(Organization.objects())
        for elem in Organization.objects():
            if elem.id == id:
                Organization.objects().pop(elem.id - 1)
            print(Organization.objects())


class Clear:
    # очистить коллекцию
    pass


class Save:
    # сохранить коллекцию в файл
    pass


class ExecuteScriptFileName:
    # считать и исполнить скрипт из указанного файла.
    # В скрипте содержатся команды в таком же виде, в котором их вводит пользователь в интерактивном режиме.
    pass


class Exit:
    # завершить программу (без сохранения в файл)
    pass


class Head:
    # вывести первый элемент коллекции
    pass


class RemoveGreater:
    # удалить из коллекции все элементы, превышающие заданный
    pass


class History:
    # вывести последние 14 команд (без их аргументов)
    pass


class MinByFullName:
    #  вывести любой объект из коллекции, значение поля fullName которого является минимальным
    # min(len(...[full_name]
    pass


class PrintFieldDescendingAnnualTurnover:
    # вывести значения поля annualTurnover всех элементов в порядке убывания
    pass


class PrintFieldDescendingPostalAddress:
    # вывести значения поля postalAddress всех элементов в порядке убывания
    pass


class SimpleCommand:
    __commands = {'help': Help,
                  'info': Info,
                  'show': Show,
                  'clear': Clear,
                  'exit': Exit}

    def __init__(self, name):
        self.__command = SimpleCommand.__commands[name]

    def execute(self):
        self.__command.execute()


class CompositeCommand:
    commands = {'add': AddElement,
                'remove': RemoveByID, }

    def __init__(self, name):
        self.__command = CompositeCommand.commands[name]

    def __read(self):
        return 1, 2, 3  # TODO: исправить с учетом понимания, какие аргументы требуются для этой команды

    def execute(self):
        args = CompositeCommand.__read(self)
        return self.__command(*args)


class Command:
    def __init__(self, name):
        if name in CompositeCommand.commands:
            self.__command = CompositeCommand(name)
        else:
            self.__command = SimpleCommand(name)

    def execute(self, *args):
        print(*args)
        self.__command.execute(*args)
