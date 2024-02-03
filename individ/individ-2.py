#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Money:
    MAX_SIZE = 10  # Максимально возможный размер списка

    def __init__(self):
        self.bills = []  # Список словарей для хранения номиналов и количества купюр
        self.size = Money.MAX_SIZE  # Максимальное количество элементов списка
        self.count = 0  # Текущее количество элементов в списке

    def add_bill(self, denomination, quantity):
        if self.count < self.size:
            for bill in self.bills:
                if bill["denomination"] == denomination:
                    bill["quantity"] += quantity
                    print(f"Уже существует купюра номиналом {denomination}, обновлено количество.")
                    return
            self.bills.append({"denomination": denomination, "quantity": quantity})
            self.bills.sort(key=lambda x: x["denomination"])  # Сортировка списка словарей по номиналу
            self.count += 1
            print(f"Добавлена купюра номиналом {denomination}, количество: {quantity}.")
        else:
            print("Достигнут максимальный размер списка, добавление невозможно.")

    def __getitem__(self, denomination):
        for bill in self.bills:
            if bill["denomination"] == denomination:
                return bill["quantity"]
        return 0  # Возвращаем 0, если купюра данного номинала отсутствует

    def __repr__(self):
        return f"Money: {self.bills}"

    def current_size(self):
        return self.count  # Возвращает текущее количество элементов в списке

if __name__ == "__main__":
    my_money = Money()
    my_money.add_bill("100", 5)
    my_money.add_bill("500", 2)
    my_money.add_bill("100", 3)  # Должно обновить количество купюр номиналом 100

    print(my_money)

    print(f"Количество купюр номиналом 100: {my_money['100']}")
    print(f"Количество купюр номиналом 1000: {my_money['1000']}")  # Должно вернуть 0, так как таких купюр нет

    print(f"Текущее количество элементов в списке: {my_money.current_size()}")
