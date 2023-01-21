# FOR LOOP
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

for key, value in person.items():
    print(f"key: {key} value: {value}")

# for key in person:
#     print(f"key: {key} value: {person[key]}")