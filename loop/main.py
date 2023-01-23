names = ["Ahamed", "Annah", "James", "Jamila"]

for name in names:
    print(name)

print('-------------------------------------')

# LOOP THROUGH DICTIONARIES

person = {
    "name": "Jamal",
    "age": 20,
    "address": "BRUSSELS"
}

print(person.items())

# Method 1
for key, value in person.items():
    print(f"key: {key} value: {value}")

# Method 2
for key in person:
    print(f"key: {key} value: {person[key]}")

print('-------------------------------------')

# Example

result = 0
numbers = [1, 2, 3, 5, 6, 7, 9]

for number in numbers:
    result += number

print(f"Result = {result}")

print('-------------------------------------')

# WHILE LOOP

number = 0

# Method 1
number = 0
while number < 10:
    print(number)
    number += 1
else:
    print("while loop ended")


# Method 2
while number < 10:
    number += 1
    if number < 5:
        continue
    print(number)


# Method 3
for n in [1, 2, 3, 4, 5, 6, 7]:
    if n == 5:
        break
    print(n)
