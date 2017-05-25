import os


class Test1():
    catalog  = []
    counrty = []
    file = open('catalog.json', 'r')
    for catalogItem in file:
        a = catalogItem
        counrty.append(a)


if __name__ == "__main__":
    pass