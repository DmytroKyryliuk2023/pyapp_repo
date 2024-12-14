# import random

LIST = [1, 3, 4, 5, 6]

def insert(pos: int, value) -> None:
    LIST.append(None)
    n = len(LIST)

    # rotate the elements to the right
    for i in range(n - 1, pos, -1):
        LIST[i] = LIST[i - 1]

    LIST[pos] = value

def main():
    print(LIST)
    insert(1, 2)
    print(LIST)
    LIST.pop()
    print(LIST)


if __name__ == "__main__":
    main()