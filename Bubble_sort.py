lst = [6, 5, 3, 1, 8, 7, 2, 4]
lenght = len(lst)
n = 0
while n < lenght:
    n += 1
    for i in range(lenght - 1):
        a = lst[i]
        b = lst[i + 1]
        if a > b:
            lst[i] = b
            lst[i + 1] = a
print(lst)
