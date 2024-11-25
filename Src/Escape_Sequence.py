# Escape Sequence are basically some special commands passed in order to make changes in the formating

#An escape sequence is a sequence of characters that, when used inside a character or string, does not represent itself but is converted into another character or series of characters that may be difficult or impossible to express directly, like newline (\n), tab (\t), and so on.
print("hello world")

# using  \n - using this the string will break or word after \n will be moved to new line
print("Hello\nworld")

# using \t will be used to give or add one tab space
print("hello\tworld")

# using \b will backspace the letter just before it
print("hello\bworld")

# lets suppose we need to print the path of a file which has \n.txt file

directory1 = 'C:\systems\program\n.txt'
directory2 = "C:\systems\program\n.txt"
print(directory1)
print(directory2)
# above code will not work and take \n as the new line rather printing it as complete directory path

# To fix above issue r should be added to keep the string or path as RAW
directory = r"C:\systems\program\n.txt"
print(directory)
