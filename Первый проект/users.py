from re import match


class User:
    def __init__(self, name, surname, patronymic, age, phone):
        self.__name = name
        self.__surname = surname
        self.__patronymic = patronymic
        self.__age = age
        self.__phone = '' # эта строчка нужна, чтобы в методе __phone_v переприсвоить (строчка 35)
        self.__phone_v(phone)

    @property
    def name(self):
        return self.__name.title()

    @property
    def surname(self):
        return self.__surname.title()

    @property
    def patronymic(self):
        return self.__patronymic.title()

    @property
    def age(self):
        return self.__age

    @property
    def phone(self):
        return self.__phone

    def __phone_v(self, phone):
        if match('[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}', phone):
            self.__phone = phone
        else:
            raise ValueError('Неправильный формат номера')

    @phone.setter
    # используем сеттер, чтобы при изменении номера произошла проверка корректности формата номера
    def phone(self, phone):
        self.__phone_v(phone)


if __name__ == '__main__':
    user = User('Иван', 'Иванов', 'Иванович', 20, '999-999-99-99')
    print(user.phone)
    try:
        user.phone = '99-999-99-98'
        print(user.phone)
    except ValueError:
        print('Неверный формат номера телефона')
    print(user)

