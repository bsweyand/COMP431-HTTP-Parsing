__author__ = "730318989"

import re
import sys


def command_is_valid(http_command):
    arguments = re.split("[ \t]", http_command.rstrip())
    try:
        if len(arguments) < 1 or arguments[0] != "GET":
            print("ERROR -- Invalid Method token.")
            return False
    except UnicodeDecodeError:
        print("ERROR -- Invalid Method token.")
        return False
    try:
        if len(arguments) < 2 or re.match('^(/\\w+)+.?\\w+$', arguments[1]) is None:
            print("ERROR -- Invalid Absolute-Path token.")
            return False
    except UnicodeDecodeError:
        print("ERROR -- Invalid Absolute-Path token.")
        return False
    try:
        if len(arguments) < 3 or re.match('^HTTP/\\d.\\d$', arguments[2]) is None:
            print("ERROR -- Invalid HTTP-Version token.")
            return False
    except UnicodeDecodeError:
        print("ERROR -- Invalid HTTP-Version token.")
        return False

    if len(arguments) > 3:
        print("ERROR -- Spurious token before CRLF.")
        return False
    return True


def process_valid_command(http_command):
    arguments = re.split("[ \t]", http_command.rstrip())
    method = arguments[0]
    path = arguments[1]
    version = arguments[2]
    print("Method = " + method)
    print("Request-URL = " + path)
    print("HTTP-Version = " + version)
    if re.search('.html|.htm|.txt|.HTML|.TXT|.HTM', path) is None:
        print("501 Not Implemented: " + path)
        return
    try:
        with open(path[1:], "r") as f:
            print(f.read().rstrip())
    except FileNotFoundError:
        print("404 Not Found: " + path)
    except IOError as e:
        print("Error: " + e)


for command in sys.stdin:
    if command == '\n':
        continue
    print(command, end="")
    if not command_is_valid(command):
        continue
    process_valid_command(command)
