# import time
import datetime
from datetime import datetime


class Server:
    def __init__(self):
        self.__messages = []

    def send_message(self, person, message):
        # self.__messages.append((person, message, time.time()))
        self.__messages.append((person, message, datetime.now().strftime('%d.%m.%Y %H:%M:%S')))
        # почему append, а не extend, если мы добавляем больше одного значения?
        return self.__messages

    @property
    def messages(self):
        # return [(elem[0].name, elem[1], elem[2]) for elem in self.__messages]  # list comprehesion
        mylist = []
        for elem in self.__messages:
            mylist.append((elem[0].name, elem[1], elem[2]))
        return mylist

#
# server = Server()
# print(server.send_message('user', 'Hi'))
# print(server.send_message('user9', 'Hi9'))

