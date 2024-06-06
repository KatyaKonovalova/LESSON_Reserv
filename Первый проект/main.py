import users
import server
import time

server = server.Server()

user1 = users.User('Иван', 'Иванов', 'Иванович', 20, '999-999-99-99')
user2 = users.User('Петр', 'Петров', 'Петрович', 25, '999-999-99-98')

print(server.send_message(user1, 'Привет'))
time.sleep(0.5)
print(server.send_message(user2, 'Привет!!!'))

print(server.messages)
