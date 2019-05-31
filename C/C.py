from sys import stdin


def main():
    addresses = [stdin.readline().strip() for _ in xrange(int(stdin.readline()))]

    s = set()

    for address in addresses[::-1]:
        if address not in s:
            print(address)
            s.add(address)


if __name__ == '__main__':
    main()
