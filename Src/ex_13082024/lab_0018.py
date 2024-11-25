'''
how to take user input ?
input function is used to take input from user
'''

# user_input =input("what is your name  ")
# print(user_input)


#try to sum two numbers using user input
# Below code wont work as you are trying to do mathematics operation on string data types and not int

# num1 =input("Enter the number ")
# num2 =input("Enter the number ")
# print("sum", num1+num2)
# print("substract", num1-num2)

#OUTPUT starts from here

# Enter the number 12
# Enter the number 8
# sum 128
# Traceback (most recent call last):
#   File "/Users/sourabhmaratha/PycharmProjects/PyATB4XLearning/Src/ex_13082024/lab_0018.py", line 15, in <module>
#     print("substract", num1-num2)
# TypeError: unsupported operand type(s) for -: 'str' and 'str'


# To make above code working one has to convert String input to Int, hence int has to be added while defining the input function



num1 = int(input("Enter the number "))
num2 = int(input("Enter the number "))
print("sum", num1 + num2)
print("subtract", num1 - num2)


