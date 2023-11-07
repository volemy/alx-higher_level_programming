#!/usr/bin/python3
"""
This writes a script that reads line by line computer metrics
"""


import sys

total_file_size = 0
status_codes = {}
valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
lines = []


def print_stats():
    """
    This prints accumulated metrics
    """
    print("File size: {}".format(total_file_size))
    for code in sorted(valid_codes):
        count = status_codes.get(code, 0)
        if count > 0:
            print("{}: {}".format(code, count))

try:
    for line in sys.stdin:
        lines.append(line.strip())
        parts = line.split()
        if len(parts) >= 7:
            total_file_size += int(parts[-1])
            status_code = parts[-2]
            if status_code in valid_codes:
                status_codes[status_code] = status_codes.get(status_code, 0) + 1


        if len(lines) == 10:
            print_stats()
            lines = []

except KeyboardInterrupt:
    print_stats()
