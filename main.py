# Variable
"""
We need input function
The input function store string
"""
name = input("Name: ")
age = input("Age: ")
age_int = int(age) + 1  # * the int function convert an string to integer
                        # ! Dont forget to add + 1

print(type(age_int))

print("Name: " + name + " age: " + age)
print(type(name))
print(type(age))

print("The next year, you will have " + str(age_int))
print(type(age_int))