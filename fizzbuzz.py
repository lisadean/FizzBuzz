def is_multiple_of_three(num):
    return num % 3 == 0

def is_multiple_of_five(num):
    return num % 5 == 0

def is_multiple_of_three_and_five(num):
    return num % 3 == 0 and num % 5 == 0

max = 100
for i in range(max):
    if is_multiple_of_three_and_five(i):
        print("FizzBuzz")
    elif is_multiple_of_three(i):
        print("Fizz")
    elif is_multiple_of_five(i):
        print("Buzz")
    else:
        print(i)