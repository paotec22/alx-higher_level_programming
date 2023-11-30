#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 1:
        print('{:d} arguments.'.format(0))
    elif len(argv) == 2:
        print('{:d} argument:'.formate(1))
    elif len(argv) > 2:
        print('{:d} argumnets:'.format(len(argv) - 1))
    if len(argv) >= 2:
        for i in argv[1:]:
            index = argv.index(i)
            print('{:d}: {}'.format(index, argv[index]))
