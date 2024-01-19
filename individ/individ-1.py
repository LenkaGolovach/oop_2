#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Поле first — целое положительное число, часы; поле second — целое полож ительное
число, минуты. Реализовать метод minutes() — приведение времени в минуты.
Максимально задействовав имеющиеся в Python средства перегрузки операторов.
"""


class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __int__(self):
        return self.hours * 60 + self.minutes

    def __str__(self):
        return f"Количество минут: {int(t)}"

    def read(self):
        hours = int(input("Введите часы: "))
        minutes = int(input("Введите минуты: "))
        self.__init__(hours, minutes)

    def display(self):
        print(str(self))

if __name__ == '__main__':
    t = Time(10, 30)
    t.display()

    t.read()
    t.display()


