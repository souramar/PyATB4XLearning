# WAP to print all numbers between 1 to 100 and wherever number is multiple of 3 print fizz
# number multiple of 5 print buzz, if number is multiple of both then print fizzbuzz

for i in range(1, 100):
    if i % 3 ==0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
