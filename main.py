from clases import *


def main():
    s = Storage
    a = Shelf('13', s)
    print(type(a.number))
    print(s.get_shelf_by_number(s, 13))


if __name__ == '__main__':
    main()
