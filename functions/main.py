# PARAMETERS AND ARGUMENTS

def greet(name, age=-1):
    print(f"Hello {name} how are you?")
    if age >= 0:
        print(f"I know your age = {age}")


greet("Jamila")
greet("John", 20)

print('-----------------------------')

# RETURN VALUES FROM FUNCTIONS


def is_adult(age):
    return age >= 18


result = is_adult(80)
print(result)

# print('-----------------------------')


def convertGender(gender="unknown"):
    if gender.upper() == "M":
        return "Male"
    elif gender.upper() == "F":
        return "Female"
    else:
        return f"Gender {gender} is unknown"


print(convertGender("F"))
print(convertGender("f"))
print(convertGender("M"))
print(convertGender("m"))
print(convertGender("hello"))


print('-----------------------------')

# BUILD IN FUNCTIONS AND IMPORT STATEMENT

from math import isqrt

print(isqrt(25))
