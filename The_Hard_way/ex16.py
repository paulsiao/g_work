from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print(f"If you don't want that, hit CTRL-C (^C).")
print(f"If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename)

print("Truncating the file. Goodbye!")
target.truncat()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("iine 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()