

def main(n, m):
        list = []
        start = 1
        while True:
            list.append(start)
            tail = ((start - 1 + (m - 1)) % n ) + 1
            if tail == 1:
                break
            start = tail
        return list

if __name__ == "__main__":
    try:
        n, m = map(int, input("введите n и m через прбед: ").split(" "))
        result = main(n, m)
        print("".join(map(str, result)))
    except ValueError:
        print("Ошибка ввода, нужно 2 числа через пробел")