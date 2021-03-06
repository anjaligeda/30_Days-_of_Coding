from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass
class MyBook(Book):
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def display (self):
        print("Title: "+str(title))
        print("Author: "+str(author))
        print("Price:",price)


title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()

'''INPUT:
The Alchemist
Paulo Coelho
248
OUTPUT:
Title: The Alchemist
Author: Paulo Coelho
Price: 248'''
