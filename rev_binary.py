import sys

def reverse(string):
    return string[::-1]

def to_binary(interger):
    return '{0:b}'.format(interger)

def to_integer(string):
    return int(string, 2)

def main():
    for line in sys.stdin:
        x = int(line)
        x = to_binary(x)
        x = reverse(x)
        x = to_integer(x)
        print x


if __name__ == "__main__":
    sys.exit(main())
