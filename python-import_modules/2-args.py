#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    nb_arg = len(sys.argv) - 1
    print("{:d}".format(nb_arg), end=' ')
    if nb_arg == 0:
        print("arguments.")
    elif nb_arg == 1:
        print("argument:")
    else:
        print("arguments:")
    if nb_arg != 0:
        for i in range(nb_arg):
            print("{:d}: {:s}".format(i + 1, sys.argv[i + 1]))
