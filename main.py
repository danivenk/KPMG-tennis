import sys

def main(argv):

    for arg in argv:
        print(arg)

    return 0

if __name__ == "__main__":
    main(sys.argv[1:])