# VARIABLES
name, full_name, PI = "Jamila", "J James", 3.14

print(name)
print(full_name)
print(PI)

print('-----------------------------------------')

brand = "Thierno"
age = 20
pi = 3.14
numbers = []
isAdult = True

print(type(brand))
print(type(age))
print(type(numbers))
print(type(pi))
print(type(isAdult))

print('-----------------------------------------')

# DYNAMICALLY TYPE

brand: str = "Thierno"
iaAdult: bool = False
def hello() -> int:
    return 1

print('-----------------------------------------')

# STRINGS
brand = 'Thierno'

print(brand.upper())
print(brand.replace('T', '20'))
print(len(brand))
print(brand != "thierno")
print("code" not in brand)

print('-----------------------------------------')

# MULTILINE AND FORMATTING STRINGS
name = "Jamila"
email = """
hello {}
how are you ?
It was nice talking to you 
"""
print(email.format(name))

print('-----------------------------------------')

# INDENTATION
import keyword
def my_function():
    name = "Maria"
    surname = "Jamila"
    
print(keyword.kwlist)
    
print('-----------------------------------------')

# ARITHMETIC OPERATORS
print(1 + 2)
print(2 * 2)
print(10 / 2)
print(9 % 2)
print(10 > 5)
print(10 <= 10)
print(10 != 10)
print(10 == 10)
print((10 > 5) and (1 < 3) and "A" == "A")
print((10 < 5) or (1 > 3) or "A" == "c")
print(not("James" == "Maria"))

print('-----------------------------------------')

# ASIGNMENT OPERATORS
number = 4
number **=2
print(number)

print('-----------------------------------------')

# IF STATEMENTS

number = 10

if not(number > 0):
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is Zero")
else:
    print(f"{number} is negative")

print('-----------------------------------------')

# QUICK WORD ON IF STATEMENTS

number = 10

if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(number)
elif number == 0:
    print(number)
elif number == 0:
    print(number)
else:
    print(f"{number} is negative")
    
print('-----------------------------------------')

# TERNARY IF STATEMENTS

number = -1
message = "positive" if number > 0 else "0 or negative"
print(message)

print('-----------------------------------------')

# LISTS & METHODS

numbers = [1, 2, 3, 4, -1, -20]

numbers.sort()
numbers.reverse()
numbers.append(1000)
print(len(numbers))
numbers.clear()
print(-20 in numbers)

# DELETING ITEMS FROM LIST

numbers.remove(-1)
numbers.pop()
numbers.pop()
del numbers[4]
print(numbers)

# SETS

numbersList = [1, 1]
numbersSet = {1, 1}
lettersSet = {"A", "A", "B", "C", "C"}
print(numbersList)
print(numbersSet)
print(lettersSet)

# SET UNION | INTERSECTION & DIFFERENCE

lettersA = {"A", "B", "C", "D"}
lettersB = {"E", "F"}
union = lettersA | lettersB
intersection = lettersA & lettersB
difference = lettersA - lettersB
print(f"Union {union}")
print(f"Intersection = {intersection}")
print(f"Difference = {difference}")

print('-----------------------------------------')


