#!/usr/bin/python3
"""
Reads from standard input and computes metrics.
"""


def print_metrics(total_size, code_counts):
    """
    Print accumulated metrics.
    """
    print("Total file size: {}".format(total_size))
    for key in sorted(code_counts):
        print("{}: {}".format(key, code_counts[key]))


if __name__ == "__main__":
    import sys

    total_size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_count = 0

    try:
        for line in sys.stdin:
            if line_count == 10:
                print_metrics(total_size, status_codes)
                line_count = 1
            else:
                line_count += 1

            parts = line.split()

            try:
                total_size += int(parts[-1])
            except (IndexError, ValueError):
                pass

            try:
                if parts[-2] in valid_codes:
                    if status_codes.get(parts[-2], -1) == -1:
                        status_codes[parts[-2]] = 1
                    else:
                        status_codes[parts[-2]] += 1
            except IndexError:
                pass

        print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
        raise
