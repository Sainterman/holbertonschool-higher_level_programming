#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv) - 1
    if args is 0:
        print("0")
    elif args is 1:
        print("{:d}".format(int(argv[1])))
    else:
        sum = 0
        for i in range(1, args + 1):
            sum += int(sys.argv[i])
        print("{:d}".format(sum))
