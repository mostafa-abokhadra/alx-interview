#!/usr/bin/python3
"""Log parsing"""


import sys
import re


def log_parsing():
    """Log parsing"""
    reg = re.compile(r"""(\d+\.\d+\.\d+\.\d+) - \[([^\]]+)\] \"GET /projects/260 HTTP/1.1\" (\d+) (\d+)""")  # noqa
    total_size = 0
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
    line_count = 0

    for line in sys.stdin:
        line_count += 1
        match = reg.match(line)

        if match:
            total_size += int(match.group(4))
            status = int(match.group(3))

            if status in status_codes:
                status_codes[status] += 1

        if line_count % 10 == 0:
            print("File size: {}".format(total_size))
            for key, value in sorted(status_codes.items()):
                if value:
                    print("{}: {}".format(key, value))

    print("File size: {}".format(total_size))
    for key, value in sorted(status_codes.items()):
        if value:
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    log_parsing()