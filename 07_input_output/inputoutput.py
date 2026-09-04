#01
name = input("Enter your name: ")
print(name)

#02
a=input("Enter your city name:")

print(f"Your city is: {a}")

#03
a=input("Enter your name:")
b=input("Enter you age:")

print(f"Your Name is: {a} and Your Age is: {b}")


#04
#input() always return string datatype

#05
a=input("Enter your Name:")
print(type(a))

#06
a=input("Enter your Name:")
b=input("Enter your age:")

print(f"Your Name is: {a} and Your Age is: {b}")

#07
a=input("Enter your Name:")
b=input("Enter your city Name:")
c=input("Enter your College Name")

print(f"Your Name is: {a} and Your Age is: {b} and Your College is: {c}" )

#08
Name= input("Enter two names: ")

a,b= Name.split()

print("First name:", a)
print("Second name:", b)

#09








# 
name = input("Enter your name: ")
print(name)

# 
city = input("Enter your city: ")
print(f"Your city is {city}")

# 
name = input("Enter your name: ")
age = input("Enter your age: ")
print(name)
print(age)

#Q4

# 
value = input("Enter any value: ")
print(type(value))


# 
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
print(first_name, last_name)

# 
name = input("Enter name: ")
city = input("Enter city: ")
college = input("Enter college: ")
print(name)
print(city)
print(college)

# 
name1, name2 = input("Enter two names separated by space: ").split()
print(name1)
print(name2)

# 
print("Q9 Answer: a = 'Python', b = 'Programming'")

# 
a, b, c = input("Enter three words : ").split()
print(a)
print(b)
print(c)


# 
num_str = "25"
num_int = int(num_str)
print(num_int, type(num_int))

# 
float_str = "25.5"
num_float = float(float_str)
print(num_float, type(num_float))

# 
num = 100
num_as_str = str(num)
print(num_as_str, type(num_as_str))

# 
user_int = int(input("Enter an integer: "))
print(type(user_int))

#
user_float = float(input("Enter a floating-point number: "))
print(type(user_float))

# 

print("Q16 Answer: input() returns strings, so '+' joins text instead of adding numbers.")

# 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a + b)


# 
name = "Rahul"
age = 20
print(f"My name is {name} and I am {age} years old.")

#
a = 10
b = 20
print(f"The sum of {a} and {b} is {a + b}")

# 
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"My name is {name} and I am {age} years old.")

# 
price = float(input("Enter the price: "))
print(f"Price: {price:.2f}")

# .
print("Q22 Answer: ':.2f' formats a float to show exactly 2 decimal places.")

#
product_name = input("Enter product name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
print(f"Product Name: {product_name}")
print(f"Price: {price}")
print(f"Quantity: {quantity}")




#
print("A", "B", "C")

# 
print("2026", "08", "19", sep="-")

#
print("Hello", end=" ")
print("World")



# 
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
total = first + second
print(f"First number: {first}")
print(f"Second number: {second}")
print(f"Sum: {total}")

# 
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
total_cost = price * quantity
print(f"Price: {price}")
print(f"Quantity: {quantity}")
print(f"Total: {total_cost:.2f}")

# 
name = input("Enter student's name: ")
age = int(input("Enter student's age: "))
marks = float(input("Enter student's marks: "))
print(f"Student Name: {name}, Age: {age}, Marks: {marks}")

# 
student_name = input("Enter student's name: ")
student_age = int(input("Enter student's age: "))
student_height = float(input("Enter student's height (in meters/cm): "))
student_city = input("Enter student's city: ")

print(f"Name: {student_name}")
print(f"Age: {student_age}")
print(f"Height: {student_height:.2f}")
print(f"City: {student_city}")