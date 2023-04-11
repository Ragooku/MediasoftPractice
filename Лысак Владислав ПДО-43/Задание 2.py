a = [1, 4, 6]
b = [11, 33, 22]

res = [x for _, x in sorted(zip(b, a))]
print(res)