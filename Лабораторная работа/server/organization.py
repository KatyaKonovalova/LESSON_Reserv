import datetime
import time


class Coordinates:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Address:
    def __init__(self, street: str, town: str):
        self.street = street
        self.town = town


class Location:
    def __init__(self, x: float, y: float, z: float, name: str):
        self.x = x
        self.y = y
        self.z = z
        self.name = name


class OrganizationType:
    COMMERCIAL = 0
    PUBLIC = 1
    GOVERNMENT = 2


class Organization:
    __id = 1
    __objects = []
    __initial_date = time.time()

    # Не понимаю, как работает присвоение id.
    # Хочу разобрать последовательность действий. Почему и как пересохраняется значение.
    def __init__(self, name: str, coordinates: Coordinates, creation_date: datetime, annual_turnover: float,
                 full_name: str, employees_count: int, type: OrganizationType, postal_address: Address
                 ):
        self.id = Organization.__id
        Organization.__id += 1
        self.name = name
        self.coordinates = coordinates
        self.creation_date = creation_date
        self.annual_turnover = annual_turnover
        self.full_name = full_name
        self.employees_count = employees_count
        self.type = type
        self.postal_address = postal_address
        Organization.__objects.append(self)

    @staticmethod
    def objects():
        return Organization.__objects

    @staticmethod
    def initial_date():
        return Organization.__initial_date
