import sys
from decimal import Decimal, getcontext


getcontext().prec = 100


def read_info_about_circle(circle: str):
    """определяем окружность"""
    with open(circle, 'r', encoding="utf-8") as fcircle:

        nums = []
        for line in fcircle:
            nums.extend(line.split())

        x0, y0 = map(Decimal, nums[:2])
        r = Decimal(nums[2])
        return x0, y0, r

        # вывод для проверки чтения файл points
def read_indo_about_point(circle: str, points: str):
    x0, y0, r = read_info_about_circle(circle)
    r2 = r * r
    """определяем точки"""
    with open(points, 'r', encoding="utf-8") as fpoints:
        for raw in fpoints:
            nums = raw.strip().split()
            x, y = map(Decimal, nums)
            if len(nums) != 2:
                continue
            x, y = map(Decimal, nums)
            d2 = (x - x0) ** 2 + (y - y0) ** 2

            if d2 == r2:
                print(0)
            elif d2 < r2:
                print(1)
            else:
                print(2)



if __name__ == '__main__':
    circle_info, points_info = map(str, sys.argv[1:3])
    try:
        read_indo_about_point(circle_info, points_info)
    except FileNotFoundError:
        print("file not found")
    except ValueError:
        print("value error")

#python task2/task2.py task2/circle.txt task2/points.txt
