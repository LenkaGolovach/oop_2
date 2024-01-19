#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Карточка иностранного слова представляет собой словарейу, содержащую иностранное
слово и его перевод. Для моделирования электронного словаря иностранных слов
реализовать класс Dictionary. Данный класс имеет поле-название словаря и содержит
список словарей WordCard, представляющих собой карточки иностранного слова. Название
словаря задается при создании нового словаря, но должна быть предоставлена
возможность его изменения во время работы. Карточки добавляются в словарь и удаляются
из него. Реализовать поиск определенного слова как отдельный метод. Аргументом
операции индексирования должно быть иностранное слово. В словаре не должно быть
карточек-дублей. Реализовать операции объединения, пересечения и вычитания словарей.
При реализации должен создаваться новый словарь, а исходные словари не должны
изменяться. При объединении новый словарь должен содержать без повторений все слова,
содержащиеся в обоих словарях-операндах. При пересечении новый словарь должен
состоять только из тех слов, которые имеются в обоих словарях-операндах. При вычитании
новый словарь должен содержать слова первого словаря-операнда, отсутствующие во втором.
"""


class WordCard:
    def __init__(self, foreign_word, translation):
        self.foreign_word = foreign_word
        self.translation = translation

    def __repr__(self):
        return f"{self.foreign_word}: {self.translation}"

    def __eq__(self, other):
        return isinstance(other, WordCard) and self.foreign_word == other.foreign_word

    def __hash__(self):
        return hash(self.foreign_word)


class Dictionary:
    MAX_SIZE = 10

    def __init__(self, name):
        self.name = name
        self.word_cards = []
        self.size = Dictionary.MAX_SIZE
        self.count = 0

    def size(self):
        return self.size  # Возвращает максимальный размер словаря

    # Создание новой карточки
    def add_word_card(self, word_card):
        if self.count < self.size:
            if word_card not in self.word_cards:
                self.word_cards.append(word_card)
                self.count += 1  #
                print(f"Добавлена карточка: {word_card}")
            else:
                print("Карточка с таким словом уже существует в словаре.")
        else:
            print("Невозможно добавить больше карточек. Достигнут максимальный размер словаря.")

    # Удаление карточки
    def remove_word_card(self, word_card):
        if word_card in self.word_cards:
            self.word_cards.remove(word_card)
            self.count -= 1
            print(f"Карточка с словом '{word_card.foreign_word}' удалена из словаря.")
        else:
            print(f"Карточка с словом '{word_card.foreign_word}' не найдена в словаре.")

    def __getitem__(self, foreign_word):
        for card in self.word_cards:
            if card.foreign_word == foreign_word:
                return card
        return None

    def __repr__(self):
        return f"Dictionary '{self.name}': {self.word_cards}"

    def union(dict1, dict2):
        new_dict = Dictionary(name=f"{dict1.name}_{dict2.name}_union")
        new_dict.word_cards = list(set(dict1.word_cards + dict2.word_cards))
        return new_dict

    def intersection(dict1, dict2):
        new_dict = Dictionary(name=f"{dict1.name}_{dict2.name}_intersection")
        new_dict.word_cards = [card for card in dict1.word_cards if card in dict2.word_cards]
        return new_dict

    def difference(dict1, dict2):
        new_dict = Dictionary(name=f"{dict1.name}_{dict2.name}_difference")
        new_dict.word_cards = [card for card in dict1.word_cards if card not in dict2.word_cards]
        return new_dict


if __name__ == "__main__":
    # Словарь 1
    dict1 = Dictionary(name="English-Russian")
    dict1.add_word_card(WordCard("hello", "привет"))
    dict1.add_word_card(WordCard("world", "мир"))

    # Добавление и удаление карточки
    dict1.add_word_card(WordCard("car", "машина"))
    dict1.remove_word_card(WordCard("car", "машина"))

    # Ссловарь 2
    dict2 = Dictionary(name="English-French")
    dict2.add_word_card(WordCard("hello", "привет"))
    dict2.add_word_card(WordCard("cat", "кошка"))
    dict2.add_word_card(WordCard("dog", "собака"))

    # Вывод содержимого словарей
    print("Словарь 1:")
    print(dict1)

    print("\nСловарь 2:")
    print(dict2)

    # Операции над словарями
    union = Dictionary.union(dict1, dict2)
    print("\nОбъединение словарей:")
    print(union)

    intersection = Dictionary.intersection(dict1, dict2)
    print("\nПересечение словарей:")
    print(intersection)

    difference = Dictionary.difference(dict1, dict2)
    print("\nВычитание словарей:")
    print(difference)
