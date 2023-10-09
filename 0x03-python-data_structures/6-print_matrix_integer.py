#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        for element in row:
            if row.index(element) != len(row) -1:
                last_char = " "
            else:
                last_char = ""
            print(str.format("{:d}", element), end=last_char)
        print()
