print('Введите число от 1 до 100')
i = int(input())
if 1 <= i <= 100:
   if not i%3 and not i%5:
       print("Fizz Buzz")
   elif not i%3:
       print("Fizz")
   elif not i%5:
       print("Buzz")
