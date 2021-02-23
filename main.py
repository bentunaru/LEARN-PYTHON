# Variable
"""

* We need input function
* The input function store string

"""
name = input("Name: ")
age = input("Age: ")

try:
    age_int = int(age) + 1  # * the int function convert an string to integer
                        # ! Dont forget to add + 1
except:
    print("ERROR : YOU NEED TO INTEGER !")
else:
    print("Your Name is : " + name + " age: " + age + "The next year, you will have " + str(age_int) + " years old")