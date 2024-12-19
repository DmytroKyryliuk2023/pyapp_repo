from typing import Type


class Subject:
    def __init__(self, name: str, credits: int):
        self.name = name
        self.credits = credits

    def printItem(self):
        print(f"Name: {self.name}, Credits: {self.credits}", end="")

class SubjectExpand(Subject):
    def __init__(self, name: str, credits: int, teacher: str):
        super().__init__(name, credits)
        self.teacher = teacher

    def printItem(self):
        super().printItem()
        print(f", Teacher: {self.teacher}", end="")


class Database:
    def __init__(self, items):
        self.items: list[Subject] = list(items)

    def add(self, item: Subject):
        self.items.append(item)

    def printItems(self):
        for item in self.items:
            item.printItem()
            print()

def main():
    item1 = Subject("Math", 6)
    item2 = SubjectExpand("OS", 5, "Pleskanka")

    database = Database((item2,))

    database.add(item1)
    database.add(item2)

    database.printItems()

if __name__ == "__main__":
    main()