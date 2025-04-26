# in range we consider the 1st number inclusive and the last number to be exclusive
x  = 0
for number in range(1,101):
    x += number

print(x)
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
       print(number)