# conditional loops works on true or false - assignment wont work

# sourabh_age = int(input("Enter age "))
#
# if (sourabh_age > 18):
#     print("Sourabh eligible to vote")
# else:
#     print("Sourabh not allowed to vote")


# #WAP to print max number
# x = int(input("Enter first number\n "))
# y = int(input("Enter second number\n"))
#
# if x>y:
#     print(x)
# else:
#     print(y)

# WAP to print max between three numbers

x = int(input("Enter first number\n "))
y = int(input("Enter second number\n"))
z = int(input("Enter third number\n "))

if x > y and x > z:
    print("max number is", x)
elif y > z and y > x:
    print("max number is", y)
else:
    print("max number is", z)
