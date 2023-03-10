# w writing a apending r reading r+ reading/writing

# file = open("./data.csv", "w")
# file = open("./data.csv", "a")
file = open("./data.csv", "r+")

file.write("id, name, email\n")
file.write("1, Jamila, jamila@gmail.com\n")
file.write("2, John, john@gmail.com\n")
file.write("3, Samir, sami@gmail.com\n")

file.close()

print('-----------------------------------')

# READING FROM FILES

file = open("./data.csv", "r")

for line in file:
    print(line)
file.close()

print('-----------------------------------')

# BETTER WAY TO WORK WITH FILES

with open("./data.csv", "r") as file:
    print(file.read())

print('-----------------------------------')

import os.path

filename = "./dataa.csv"

if os.path.isfile(filename):
    with open(filename, "r") as file:
        print(file.read())
else:
    print(f"file {filename} does not exist")
