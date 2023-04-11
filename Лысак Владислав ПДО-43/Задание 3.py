def common_chars(a):
    common = set(a[0])
    for i in a[1:]:
        common &= set(i)
    result = list(common)
    result.sort(key = lambda x: [i.count(x) for i in a])
    return result

a = ["cool", "lock", "cook"]
result = common_chars(a)
print(result)