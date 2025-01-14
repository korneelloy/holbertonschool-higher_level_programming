#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    nb_arg = len(sys.argv) - 1
    result = 0
    for i in range(nb_arg):
        result = result + int(sys.argv[i + 1])
    print("{:d}".format(result))
