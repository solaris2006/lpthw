from sys import argv

script, filename = argv

print(f"We're  going to erase {filename}.")
print("If you don't want that , hit crtl-c")
print("If you do want that, hit return ")

input("?")


target = open(filename, 'w')

print("Opening the file...")


print("Truncating the file GoodBye!")

target.truncate()


print("now I am going to assk you for three lines.")


line1 = input("line1: ")
line2 = input("line1: ")
line3 = input("line1: ")

print("I am going to write thes to  a file ")

target.write(line1, "\n", line2 , "\n", line3 , "\n")

print("And finally we close it")

target.close()
