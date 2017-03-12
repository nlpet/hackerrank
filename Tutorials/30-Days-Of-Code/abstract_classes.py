"""
Day 13: Abstract Classes

URL: https://www.hackerrank.com/challenges/30-abstract-classes
"""
from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display():
        pass


class MyBook(Book):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print('Title: {}'.format(self.title))
        print('Author: {}'.format(self.author))
        print('Price: {}'.format(self.price))


def main():
    title = input()
    author = input()
    price = int(input())
    new_novel = MyBook(title, author, price)
    new_novel.display()


if __name__ == '__main__':
    main()
