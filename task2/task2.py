import os
from decimal import Decimal, getcontext


getcontext().prec = 100
value_list = []
dot_list = []


def read_info_about_circle(name1: str, name2: str):
    try:
        with open(name1, 'r', encoding="utf-8") as fdots, \
        open(name2, "r", encoding="utf-8") as fcircle:
            #вывод для проверки чтения файл circle x0 y0 r
            for line in fcircle.readlines():
                for value in line.split():
                    value_list.append(int(value))
            x1 = value_list[0]
            y1 = value_list[1]
            r = value_list[2]
            # вывод для проверки чтения файл points
            for line in fdots:
                parts = line.strip().split()
                if len(parts) == 2:
                    x, y = Decimal(parts[0]), Decimal(parts[1])
                    dot_list.append((x, y))
            
            for x, y in dot_list:
                dist_sq = (x - x1) ** 2 + (y - y1) ** 2
                r_sq = r ** 2

                if dist_sq == r_sq:
                    print(0)
                elif dist_sq < r_sq:
                    print(1)
                else:
                    print(2)
    except FileNotFoundError:
        print("file error")


if __name__ == '__main__':
    name1 = "points.txt"
    name2 = "circle.txt"
    read_info_about_circle(name1, name2)