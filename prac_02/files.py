out_file = open("name.txt", "w")
name = input("Enter name: ")
print(name, file=out_file)
out_file.close()

in_file = open("name.txt", "r")
name = in_file.read()
print("Your name is", name)
in_file.close()

in_file = open("numbers.txt", "r")
first_number = in_file.readline()
second_number = in_file.readline()
print(int(first_number) + int(second_number))
in_file.close()

