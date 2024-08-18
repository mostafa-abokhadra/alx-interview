#!/usr/bin/env python3
""" log parsing
"""


# import functools
# import sys
# def add(a, b):
#     """add 2 numbers
#     """
#     return a + b
# def metrics():
#     """
#     <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
#     <status code> <file size>
#     127.0.0.1 - [1/1/2024] "GET /projects/260 HTTP/1.1" 200 4000
#     """
#     counter = 0
#     stausCodes = [200, 301, 400, 401, 403, 404, 405, 500]
#     fileSizes = [0, 0]
#     statusNumbers = {}
#     try:
#         for line in sys.stdin:
#             splitted = line.split()
#             if not len(splitted) == 9:
#                 continue
#             else:
#                 fileSizes.append(int(splitted[-1]))
#                 try:
#                     status = int(splitted[-2])
#                     if status not in stausCodes:
#                         continue
#                     if status in statusNumbers.keys():
#                         statusNumbers[status] += 1
#                     else:
#                         statusNumbers[status] = 1
#                 except Exception as err:
#                     continue
#             counter += 1
#             if counter == 10:
#                 break
#     except KeyboardInterrupt:
#         pass
#     print("File size: {}".format(functools.reduce(add, fileSizes)))
#     for key, value in sorted(statusNumbers.items()):
#         print("{}: {}".format(key, value))
# if __name__ == '__main__':
#     metrics()
import sys


if __name__ == '__main__':

    filesize, count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in codes}

    def print_stats(stats: dict, file_size: int) -> None:
        print("File size: {:d}".format(filesize))
        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass
            try:
                filesize += int(data[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                print_stats(stats, filesize)
        print_stats(stats, filesize)
    except KeyboardInterrupt:
        print_stats(stats, filesize)
        raise
