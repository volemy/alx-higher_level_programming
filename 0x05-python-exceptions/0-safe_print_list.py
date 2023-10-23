#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    number_items = 0
    for idx in range(x):
        try:
            print(my_list[idx], end="")
            number_items += 1
        except IndexError:
            break
    print()
    return number_items
