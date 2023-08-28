__author__ = "730318989"

import re


def command_is_valid(command):
    arguments = re.split("[ \t]+", command)
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


