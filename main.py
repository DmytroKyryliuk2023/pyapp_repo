import random

def main():
    list1 = [random.randint(1, 10) for i in range(10)]
    list2 = [random.randint(1, 10) for i in range(10)]
    list3 = list1 + list2
    print(list3)

if __name__ == "__main__":
    main()