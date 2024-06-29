class ProviderCommunication:
    def receive(self):
        print('Получение продукции от производителя')

    def payment(self):
        print('Оплата поставщику с удержанием комиссии за продажу продукции')


class Site:
    def placement(self):
        print('Размещение на сайте')

    def delete(self):
        print('Удаление с сайта')


class Database:
    def insert(self):
        print('Запись в базу данных')

    def delete(self):
        print('Удаление из базы данных')


class MarketPlace:  # Видимо это фасад
    def __init__(self):
        # Здесь создаются protected поля класса MarketPlace, каждой их которых присваивается класс описанный выше
        # И вместе с этим дается доступ ко всем методам класса
        self._provider_communication = ProviderCommunication()
        self._site = Site()
        self._database = Database()

    def product_receipt(self):
        self._provider_communication.receive()  # класс ProviderCommunication() метод receive()
        self._site.placement()  # класс Site() метод placement()
        self._database.insert()  # класс Database() метод insert()

    def product_release(self):
        self._provider_communication.payment()
        self._site.delete()
        self._database.delete()


"""Главный вопрос! Зачем?"""

# Чтобы была возможность при вызове одного метода одновременно совершать несколько действий? Паттернов?
# То есть если всегда после получения продукции от производителя, мы дальше добавляем в БД и размещаем на сайте
# То не имеет смысла вызывать каждый метод, а создать один метод, который сразу будет последовательно вызывать все три

# Это делается для удобства пользователя? Чтобы ему не приходилось взаимодействовать с методами напрямую?
# Фасад получает запрос, и делегирует его другим классам.

if __name__ == '__main__':
    market_place = MarketPlace()
    market_place.product_receipt()
    print()
    market_place.product_release()


