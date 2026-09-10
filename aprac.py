print("""we're \n in kalol""")

A="dev"
B="Dev"

print(A==B)


a="python"

print(a[:5])

print(a[0:6:2])

print(a[::1])

print(a[::-1])

#lenght
print(len(a))

print(len("python"))

A="1234567890"

print(len(A))


##27-8-2026

b="python"
c=b

c=(b[:])

a="python"
print(a.upper()[0:3] + a.lower()[3:])


name = "python"
print(name.upper())


name = "PYTHON"
print(name.lower())


text = "pYTHON PROGRAMMING"
print(text.capitalize())

text = "python programming language"
print(text.title())

text = "Python"
print(text.swapcase())

text = "HELLO"
print(text.casefold())

message = "Hello Python"
print("Python" in message)
print("Java" in message)
print("Java" not in message)
print(message.find("Python"))

#31-08-2026
text= "Hello Python"

print(text.index("Python"))

Text="hiiii"

print(Text.count("i"))

name= "Python Programming"

print(name.startswith("Python"))

file = "notes.txt"

print(file.endswith(".txt"))

text="python"

print("python" in text)

a="python"

print(text==a)

#1-09-2026

a="python programming"
b="python Programming"

c=b.lower() in a.lower()

print(c)

text="hello"
text1=" hello "

print(text == text1.strip())

#
print("He said \"Hello\"")

#
name = "John"
age = 20

print(f"My name is {name} and I am {age} years old.")


########  imp

text="apple,banana,cherry"
print(text.split(","))

print(text)

print(not "")

a,b=map(int,input("Enter two numbers:").split())

print(a,b ,type(a),type(b))


a,b=input("Enter two numbers:").split()

print(a,b)

a,b=map(int,input("Enter two numbers:").split())

print(a,b ,type(a),type(b))

name=input("Enter your Name:")
age=input("Enter your Age:")
lab=input("Enter your lab Number:")
product_name=input("Enter Prooduct Name:")
product_prize=input("Enter Product Prize:")
count=input("Enter product Count:")
Total_prize=int(product_prize)*int(count)

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Lab Number: {lab}")
print(f"Product Name: {product_name}")
print(f"Product Prize: {product_prize}")
print(f"Product Count: {count}")
print(f"Total Prize: {Total_prize}")

print(type(name))
print(type(age))
print(type(lab))


a,b=input("Enter two numbers:").split()

print(a,b)
