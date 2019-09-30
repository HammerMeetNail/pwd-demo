import sys


def add(num1, num2):
    return num1 + num2

if __name__ == '__main__':

    if len(sys.argv) <= 2:
        total = add(10, 10)
    else:
        num1 = sys.argv[1]
        num2 = sys.argv[2]

        total = add(int(num1), int(num2))
    print(total)
