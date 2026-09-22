##Q1

text = input("Enter a string: ")

uppercase = 0
lowercase = 0
digits = 0
spaces = 0
special = 0

for ch in text:
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special += 1

print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)

counts = {
    "Uppercase": uppercase,
    "Lowercase": lowercase,
    "Digits": digits,
    "Spaces": spaces,
    "Special characters": special
}

highest = max(counts.values())

if list(counts.values()).count(highest) > 1:
    print("Tie")
else:
    for category, count in counts.items():
        if count == highest:
            print("Highest category:", category)
##Q2

fail_count = 0
pass_count = 0
good_count = 0
excellent_count = 0

for i in range(1, 11):
    marks = int(input(f"Enter marks for student {i}: "))
    if marks < 35:
        print("Fail")
        fail_count += 1
    elif marks <= 49:
        print("Pass")
        pass_count += 1
    elif marks <= 74:
        print("Good")
        good_count += 1
    elif marks <= 100:
        print("Excellent")
        excellent_count += 1

print(f"Fail count: {fail_count}")
print(f"Pass count: {pass_count}")
print(f"Good count: {good_count}")
print(f"Excellent count: {excellent_count}")

#Q3

