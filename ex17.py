from sys import argv
from os.path import exists

script, from_file, to_file = argv


print(f"Copying {from_file} to {to_file}")


in_data = in_file = open(from_file).read()

print(f"Does the file exist? {exists(to_file)}")
input()

out_file=open(to_file, 'w')
out_file.write(in_data)
print("Allright, all done. ")

out_file.close()
