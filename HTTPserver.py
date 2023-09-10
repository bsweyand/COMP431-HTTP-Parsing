__author__ = "730318989"

import re


def command_is_valid(http_command):
    arguments = re.split("[ \t]+", http_command)
    if len(arguments) < 1 or arguments[0] != "GET":
        print("ERROR -- Invalid Method token.")
        return False
    elif len(arguments) < 2 or re.match('^(/\w+)+$', arguments[1]) is None:
        print("ERROR -- Invalid Absolute-Path token.")
        return False
    elif len(arguments) < 3 or re.match('^HTTP/\d.\d$', arguments[2]) is None:
        print("ERROR -- Invalid HTTP-Version token.")
        return False
    elif len(arguments) > 3:
        print("ERROR -- Spurious token before CRLF.")
        return False
    return True


def process_valid_command(http_command):
    arguments = re.split("[ \t]+", http_command)
    method = arguments[0]
    path = arguments[1]
    version = arguments[3]
    print("Method = " + method)
    print("Request-URL = " + path)
    print("HTTP-Version = " + version)
    if re.match("\\.htm$|\\.html$|\\.txt$", path) is None:
        print("501 Not Implemented: " + path)
        return
    try:
        with open(path, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("404 Not Found: " + path)
    except IOError as e:
        print("Error: " + e)


# split input into separate commands
command_list = []
while True:
    try:
        line = input()
    except EOFError:
        break
    command_list.append(line)

for command in command_list:
    print(command)
    if not command_is_valid(command):
        print()
        continue
