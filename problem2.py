#!/usr/bin/python3

def even_fibonaccis():
    total = 0
    cur = 2
    prev = 1

    while cur <= 4000000:
        if cur % 2 == 0:
            total += cur
        cur += prev
        prev = cur - prev

    print(total)

if __name__ == '__main__':
    even_fibonaccis()
