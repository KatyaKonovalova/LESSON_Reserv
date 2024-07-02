import datetime
from datetime import datetime


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
    __initial_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Не понимаю, как работает присвоение id.
    # Хочу разобрать последовательность действий. Почему и как пересохраняется значение.
    # def __init__(self, name: str, coordinates: Coordinates, creation_date: datetime, annual_turnover: float,
    #              full_name: str, employees_count: int, type: OrganizationType, postal_address: Address
    #              ):
    def __init__(self, name: str, full_name: str, employees_count: int, annual_turnover: float):
        self.id = Organization.__id
        Organization.__id += 1
        self.name = name
        # self.coordinates = coordinates
        # self.creation_date = creation_date
        self.annual_turnover = annual_turnover
        self.full_name = full_name
        self.employees_count = employees_count
        # self.type = type
        # self.postal_address = postal_address
        Organization.__objects.append(self)

    @staticmethod
    def objects():
        return Organization.__objects

    @staticmethod
    def initial_date():
        return Organization.__initial_date

    @staticmethod
    def id():
        return Organization.__id


# class CollectionManager:
#     def __init__(self):
#         self.__collection = Organization.objects()
#
#     def elem(self):
#         return str(self.__collection)


org1 = Organization('1', 'Машиностроительный завод', 100, 1.1)
org2 = Organization('2', 'Кондитерская', 5, 2.2)
org3 = Organization('3', 'Столовая', 10, 3.3)
org4 = Organization('4', 'Ресторанный дворик', 50, 4.4)
# print(org1.id, org2.id)
# print(Organization.objects())

# s = "remove by id, 1, j, 8"
# print(s[s.find(",") + 1:])
#
# a = 'remove by id, 1, 2'
# print(','.join(a.split(',')[:-1]))

# print('2.2' > '2')