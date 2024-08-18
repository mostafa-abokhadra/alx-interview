#!/usr/bin/env python3
""" log parsing
"""
import functools
import sys


def add(a, b):
    """add 2 numbers
    """
    return a + b


def metrics():
    """
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size>
    127.0.0.1 - [1/1/2024] "GET /projects/260 HTTP/1.1" 200 4000
    """
    counter = 0
    stausCodes = [200, 301, 400, 401, 403, 404, 405, 500]
    fileSizes = [0, 0]
    statusNumbers = {}
    try:
        for line in sys.stdin:
            splitted = line.split()
            if not len(splitted) == 9:
                continue
            else:
                fileSizes.append(int(splitted[-1]))
                try:
                    status = int(splitted[-2])
                    if status not in stausCodes:
                        continue
                    if status in statusNumbers.keys():
                        statusNumbers[status] += 1
                    else:
                        statusNumbers[status] = 1
                except Exception as err:
                    continue
            counter += 1
            if counter == 10:
                break
    except KeyboardInterrupt:
        pass
    print("File size: {}".format(functools.reduce(add, fileSizes)))
    for key, value in sorted(statusNumbers.items()):
        print("{}: {}".format(key, value))


if __name__ == '__main__':
    metrics()
