#!/usr/bin/python3
import sys

if __name__ == "__main__":

    num = len(sys.argv)
    if num == 1:
        print("{} arguments.".format(num - 1))
    elif num == 2:
        print("{} argument:".format(num - 1))
        for i in range(1, num):
            print("{}: {}".format(i, sys.argv[i]))
    else:
        print("{} arguments:".format(num - 1))
        for i in range(1, num):
            print("{}: {}".format(i, sys.argv[i]))
