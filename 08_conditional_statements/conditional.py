

# 1
number = int(input("Enter a number: "))
if number > 10:
    print("Greater than 10")

# 2
age = int(input("Enter age: "))
if age >= 18:
    print("Adult")

# 3
number = int(input("Enter a number: "))
if number > 0:
    print("Positive")

# 4
marks = int(input("Enter marks: "))
if marks >= 40:
    print("Pass")

# 5
number = int(input("Enter a number: "))
if number == 0:
    print("Zero")



# 6
number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
else:
    print("Not positive")

# 7
age = int(input("Enter age: "))
if age >= 18:
    print("Adult")
else:
    print("Minor")

# 8
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# 9
marks = int(input("Enter marks: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")

# 10
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print(f"{num1} is greater")
else:
    print(f"{num2} is greater")



# 11
marks = int(input("Enter marks: "))
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("F")

# 12
number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# 13
day = int(input("Enter day number: "))
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
else:
    print("Other")

# 14
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Excellent")
elif marks >= 60:
    print("Good")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")



# 15
number = int(input("Enter a number: "))
if number == 1:
    print("1")
elif number == 2:
    print("2")
elif number == 3:
    print("3")
else:
    print("Other")


# 16
age = int(input("Enter age: "))
if age >= 18:
    if age <= 60:
        print("Between 18 and 60")

# 17
marks = int(input("Enter marks: "))
if marks >= 40:
    if marks >= 75:
        print("Good")
    else:
        print("Passed")
else:
    print("Failed")

# 18
number = int(input("Enter a number: "))
if number > 0:
    if number > 100:
        print("Positive and greater than 100")
    else:
        print("Positive but not greater than 100")

# 19
age = int(input("Enter age: "))
if age >= 18:
    if age >= 60:
        print("Senior citizen")
    else:
        print("Adult")
else:
    print("Minor")

# 20
number = int(input("Enter a number: "))
if number != 0:
    if number > 0:
        print("Positive")
    else:
        print("Negative")
else:
    print("Zero")



# 21
age = int(input("Enter age: "))
marks = int(input("Enter marks: "))
if age >= 18 and marks >= 40:
    print("Eligible")

# 22
number = int(input("Enter a number: "))
if number < 10 or number > 100:
    print("Special")

# 23
age = int(input("Enter age: "))
has_id = bool(input("Has ID? (leave blank for False, anything for True): "))
if age >= 18 and has_id is True:
    print("Allowed")

# 24
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > 10 and num2 > 10:
    print("Both are greater than 10")

# 25
number = int(input("Enter a number: "))
if number < 0 or number > 100:
    print("Number is out of the 0-100 range")




# 26
is_closed = False
if not is_closed:
    print("Open")

# 27
number = int(input("Enter a number: "))
if number >= 10 and number <= 50:
    print("Number is between 10 and 50")

# 28
number = int(input("Enter a number: "))
if number < 10 or number > 50:
    print("Number is outside the range 10 to 50")

# 29
is_student = True
has_id = True
has_ticket = True
if is_student and has_id and has_ticket:
    print("Allowed")

# 30
age = int(input("Enter age: "))
marks = int(input("Enter marks: "))
has_id = True  # example value; replace with actual input logic as needed
if age >= 18 and marks >= 40 and has_id is True:
    print("Eligible")
else:
    print("Not eligible")

# Explanation for Q30:
# 'and' is appropriate here because eligibility depends on ALL three
# conditions being true at the same time (age requirement, marks
# requirement, and having a valid ID). If any single condition fails,
# the person should NOT be eligible. 'and' only evaluates to True when
# every condition on both sides is True, which exactly matches this
# requirement. Using 'or' instead would incorrectly make a person
# eligible even if they satisfied just one condition.