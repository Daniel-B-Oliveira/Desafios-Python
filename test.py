n = int(input("n = "))

"""
1
*2 + 1

"""

while True:
    if n % 2 == 0:
        m = int(n/2)
        print(f"{n} / 2 = {m}")
        n = m
    else:
        m = int(n*3 + 1)
        print(f"{n} * 3 + 1 = {m}")
        n = m
    if n == 1:
        break