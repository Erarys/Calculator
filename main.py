# Task car
import time


class myList(list):
    """
    Под класс MyList, Родитель: list
    """
    def index(self, value, **kwargs):
        """
        Метод для получения индекса числа в списке

        :param value: значение которое нужно проверить
        :param kwargs:
        :return: int
        :rise ValueError: если значение value отсутствует внутри списка
        """
        try:
            return super().index(value)
        except ValueError:
            print("Такого направления не существует")


class Car:
    """
    Базовый класс, описывающий транспорт(машину).

    Attributes:
        x (int): кординаты машины по оси - x
        y (int): кординаты машины по оси - y
        direction: основыне направления которому смотрит машина

    Attributes:
        direction_list (list): основыне направление
    """
    direction_list = myList(["North", "East", "South", "West"])

    def __init__(self, x=0, y=0, direction="North"):
        self.__x = x
        self.__y = y
        self.__direction = None

        self.set_degree(direction)

    def get_position(self):
        """
        Геттер для получения общей информаций машины
        :return: str.format(
            self.__class__.__name__: имя класса экземпляра
            self.__x: кординат по оси x
            self.__y: кординат по оси y
            self.__direction: оснавная направления машины
        )
        """
        return "Положение {} находиться ({}, {}) по направлению на {}\n{}".format(
            self.__class__.__name__,
            self.__x,
            self.__y,
            self.__direction,
            self
        )

    def advanced_setting_degree(self):
        """
        Метод для поворота машины
        """
        while True:
            print(self.get_position())
            turn = int(input("-1 - в лево, 1 - в право (2-stop): "))

            # Чтобы остановить цикл
            if turn == 2:
                break

            # Находим индекс направлени в списке направлений
            index = self.direction_list.index(self.get_degree())
            # Получаем следущее значение по списку
            value = self.direction_list[(index + turn) % 4]
            self.set_degree(value)

    def drive(self, size):
        """
        Метод для запуска машины
        :param size: кол-во итераций
        :type size: int
        """
        sign = 1
        degree_index = self.direction_list.index(self.get_degree())
        # Если наш знак находиться выше в списке
        if degree_index > 1:
            sign = - 1

        print("Машина едет...")
        for _ in range(size):
            if degree_index % 2:
                self.set_x(self.get_x() + sign)
            else:
                self.set_y(self.get_y() + sign)
            print(self.get_position())

    def set_degree(self, direction):
        """
        Сеттер для установки направления

        :param direction:
        :type direction: str
        """
        # Проверяем корекность аргумента
        if self.direction_list.index(direction.title()) is not None:
            self.__direction = direction.title()

    def set_x(self, xValue):
        self.__x = xValue

    def set_y(self, yValue):
        self.__y = yValue

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_degree(self):
        return self.__direction


class Bus(Car):
    """
    Класс Bus, Родитель (Car)

    Args:
        money (int): Кол-во денег
        count_passengers (int): Кол-во пассажиров
    """
    def __init__(self, money=0, count_passengers=0):
        super().__init__()

        self.__money = money
        self.__count_passengers = count_passengers

    def __str__(self):
        return "Пассажиров {}, денег {}".format(
            self.get_count_passengers(),
            self.get_money()
        )

    def drive(self, size, price):
        """
        Метод с перегрузкой. Отвечает за получение денег с пассажиров.
        :param size: кол-во итераций (дороги)
        :param price: цена за 1 итерацию (км)
        """
        sign = 1
        degree_index = self.direction_list.index(self.get_degree())
        # Если наш знак находиться выше в списке
        if degree_index > 1:
            sign = - 1

        print("Машина едет...")
        for _ in range(size):
            if degree_index % 2:
                self.set_x(self.get_x() + sign)
            else:
                self.set_y(self.get_y() + sign)
            self.set_money(self.get_count_passengers() * price)
            print(self.get_position())

    def come(self, count):
        """
        Метод отвечает за приход пассажиров
        :param count: кол-во пассажиров
        """
        self.__count_passengers += count

    def out(self, count):
        """
        Метод для вычитание пассажиров
        :param count: кол-во выходящих пассажиров
        """

        # Проверяем достаточно ли общих пассажиров
        if self.get_count_passengers() - count >= 0:
            self.__count_passengers -= count
        else:
            print("Не допустимое кол-во ушедших")
            print(self.get_position())

    def get_money(self):
        return self.__money

    def set_money(self, money):
        self.__money += money

    def get_count_passengers(self):
        return self.__count_passengers


if __name__ == "__main__":
    myBus = Bus()

    while True:
        actions = int(input("Введите: (0: настройка направления, \n1: ехать прямо, 2: настройки для автобуса): "))
        print()
        if actions == 0:
            myBus.advanced_setting_degree()
        elif actions == 1:
            drive_len = int(input("Введите сколько ехать? "))
            price = int(input("Цена за один км: "))
            myBus.drive(drive_len, price)
        elif actions == 2:
            bus_action = int(input("Введите: (0: вышли, 1: вошли) из автобуса: "))
            count = int(input("Кол-во человек: "))
            if bus_action == 0:
                myBus.out(count)
            elif bus_action == 1:
                myBus.come(count)

        print()