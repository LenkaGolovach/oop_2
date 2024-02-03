#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Pair:
    def __init__(self, first=0, second=0):
        self.first = int(first)
        self.second = int(second)
        if self.first >= self.second:
            raise ValueError("Значение 'first' должно быть меньше 'second'.")

    def read(self, prompt=None):
        line = input(prompt if prompt else "Введите интервал через запятую (например, '5,10'): ")
        parts = list(map(int, line.split(',', maxsplit=1)))
        if parts[0] >= parts[1]:
            raise ValueError("Первое значение должно быть меньше второго.")
        self.first, self.second = parts

    def display(self):
        print(f"[{self.first}, {self.second})")

    def __contains__(self, item):
        """Проверка принадлежности элемента интервалу с использованием оператора in."""
        return self.first <= item < self.second

    def __add__(self, other):
        """Добавление секунд к интервалу."""
        if isinstance(other, int):
            return Pair(self.first, self.second + other)
        raise ValueError("Можно добавлять только целые числа.")

    def __sub__(self, other):
        """Вычитание секунд из интервала."""
        if isinstance(other, int):
            return Pair(self.first, max(self.first, self.second - other))
        raise ValueError("Можно вычитать только целые числа.")

    def __eq__(self, other):
        """Сравнение двух интервалов на равенство."""
        if isinstance(other, Pair):
            return self.first == other.first and self.second == other.second
        return False

    def __lt__(self, other):
        """Сравнение, меньше ли один интервал другого."""
        if isinstance(other, Pair):
            return self.second <= other.first

if __name__ == '__main__':
    pair = Pair(0, 10)
    pair.display()

    pair.read("Введите интервал: ")
    pair.display()

    value = int(input("Введите значение для проверки принадлежности к интервалу: "))
    if value in pair:
        print(f"Значение {value} находится в интервале.")
    else:
        print(f"Значение {value} находится вне интервала.")

    # Демонстрация добавления и вычитания
    new_pair = pair + 5
    new_pair.display()

    new_pair = pair - 3
    new_pair.display()

    # Демонстрация сравнения интервалов
    another_pair = Pair(5, 15)
    if pair == another_pair:
        print("Интервалы равны.")
    elif pair < another_pair:
        print("Первый интервал меньше второго.")
    else:
        print("Первый интервал не меньше и не равен второму.")


