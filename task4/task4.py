import os
import sys


def task4(filename: str):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.readlines()
            numbers = []
            for num in content:
                if num.strip() != "":
                    numbers.append(int(num))

        numbers.sort()

        le = len(numbers)
        middle = le // 2
        median = numbers[middle]

        total = 0

        for num in numbers:
            total += abs(median - num)

        return total

    except FileNotFoundError:
        print("Файл не найден")


if __name__ == "__main__":
    name = sys.argv[1]
    result = task4(name)
    print(result)
