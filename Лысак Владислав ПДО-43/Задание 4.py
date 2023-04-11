# Задание 4 Римские цифры
a = {'M':1000, 'D':500, 'C':100,'L':50, 'X':10, 'V':5, 'I':1,}
def to_chislo(num):
    roman = 0
    key = num[-1]
    for i in num[::-1]:
        if a[i] >= a[key]:
            roman += a[i]
            key = i
        else:
            roman -= a[i]
    return roman

print(to_chislo('XV')) #Сюда нужно ввести римское число