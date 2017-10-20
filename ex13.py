from sys import argv

print("Please enter the first argument")
name = input(">")
print("Please enter the second argument")
surname = input(">")

print("Please enter the third argument")
middlename = input(">")


script, first, second, third = argv

print("The script is called: ", script)
print("The first variable is: ", first + name)
print("Your second variable is: ", second + surname)
print("Your third variable is: ", third + middlename)

