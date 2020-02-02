# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 13:48:56 2018

@author: southorn
"""

list4 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']


def main():
    list5 = [2, 7, 8, 4, 6, 1, 3, 5]
    list4.sort()
    print  # _list(list4)
    list5.sort()
    print(list5)
    # list4.sort(key=len)
    print(list4)


def print_list(o):
    for i in o:
        print(i, end=' ', flush=True)
        print()


if __name__ == '__main__':
    main()
    print_list(list4)
