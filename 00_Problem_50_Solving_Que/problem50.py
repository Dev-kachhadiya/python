##Q1

text = input("Enter a string: ")

uppercase = 0
lowercase = 0
digits = 0
spaces = 0
special = 0

for a in text:
    if a.isupper():
        uppercase += 1
    elif a.islower():
        lowercase += 1
    elif a.isdigit():
        digits += 1
    elif a == " ":
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

sentence = input("Enter a sentence: ")
words = sentence.split()

highest_score = -1
highest_word = ""

for word in words:
    current_score = 0
    for a in word:
        if a.lower() in "aeiou":
            current_score += 2
        elif a.isalpha():
            current_score += 1
        elif a.isdigit():
            current_score += 3
        else:
            current_score += 4
    
    if current_score > highest_score:
        highest_score = current_score
        highest_word = word

print(f"Word with highest score: '{highest_word}' with a score of {highest_score}")

#Q4

for i in range (5):
    passsword=int(input("Enter a password:"))


    # Q4. Password Batch Validator
# =====================================================================
for i in range(1, 6):
    password = input(f"Enter password for user {i}: ")
    
    length_ok = len(password) >= 8
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    for letter in password:
        if letter.isupper():
            has_upper = True
        elif letter.islower():
            has_lower = True
        elif letter.isdigit():
            has_digit = True
        else:
            has_special = True
            
    conditions_met = 0
    if length_ok: conditions_met += 1
    if has_upper: conditions_met += 1
    if has_lower: conditions_met += 1
    if has_digit: conditions_met += 1
    if has_special: conditions_met += 1
    
    if conditions_met == 5:
        print("Strong")
    elif conditions_met >= 3:
        print("Medium")
    else:
        print("Weak")


# =====================================================================
# Q5. Sentence Word Analyzer
# =====================================================================
sentence = input("Enter a sentence: ")
words = sentence.split()

short_words = 0
medium_words = 0
long_words = 0

for word in words:
    word_len = len(word)
    print(f"Word: '{word}', Length: {word_len}")
    
    if word_len <= 3:
        print("Classification: Short")
        short_words += 1
    elif word_len <= 6:
        print("Classification: Medium")
        medium_words += 1
    else:
        print("Classification: Long")
        long_words += 1

print(f"Total Short Words: {short_words}")
print(f"Total Medium Words: {medium_words}")
print(f"Total Long Words: {long_words}")


# =====================================================================
# Q6. Number-String Conversion Challenge
# =====================================================================
for i in range(1, 6):
    num = int(input(f"Enter number {i}: "))
    num_str = str(num)
    
    even_digits = 0
    odd_digits = 0
    
    for digit in num_str:
        if digit.isdigit():
            if int(digit) % 2 == 0:
                even_digits += 1
            else:
                odd_digits += 1
                
    if even_digits > odd_digits:
        print("Even digits occur more.")
    elif odd_digits > even_digits:
        print("Odd digits occur more.")
    else:
        print("Equal")



# Q7. Repeated Character Report

text = input("Enter a string: ")
processed_letters = ""

for letter in text:
    if letter not in processed_letters:
        # Manually count occurrences without using .count()
        occurrences = 0
        for track in text:
            if track == letter:
                occurrences += 1
                
        if occurrences > 1:
            classification = ""
            if occurrences == 2:
                classification = "Duplicate"
            elif occurrences <= 4:
                classification = "Repeated"
            else:
                classification = "Highly Repeated"
            
            print(f"Letter '{letter}' appears {occurrences} times -> {classification}")
            processed_letters += letter



# Q8

total_amount = 0
budget_count = 0
regular_count = 0
premium_count = 0
luxury_count = 0

for i in range(1, 9):
    price = float(input(f"Enter price for product {i}: "))
    total_amount += price
    
    if price < 500:
        budget_count += 1
    elif price <= 1999:
        regular_count += 1
    elif price <= 4999:
        premium_count += 1
    else:
        luxury_count += 1

average_price = total_amount / 8

print(f"Total Amount: ₹{total_amount}")
print(f"Budget Products: {budget_count}")
print(f"Regular Products: {regular_count}")
print(f"Premium Products: {premium_count}")
print(f"Luxury Products: {luxury_count}")
print(f"Average Product Price: ₹{average_price}")



# Q9

text = input("Enter a string: ")

vowel_count = 0
consonant_count = 0
digit_count = 0
special_count = 0

for pos in range(len(text)):
    letter = text[pos]
    
    # Check position odd or even
    if pos % 2 == 0:
        pos_type = "Even"
    else:
        pos_type = "Odd"
        
    # Check element category
    if letter.lower() in "aeiou":
        letter_type = "Vowel"
        vowel_count += 1
    elif letter.isalpha():
        letter_type = "Consonant"
        consonant_count += 1
    elif letter.isdigit():
        letter_type = "Digit"
        digit_count += 1
    else:
        letter_type = "Special Character"
        special_count += 1
        
    print(f"Letter: '{letter}' | Position: {pos} ({pos_type}) | Type: {letter_type}")

print(f"Summary -> Vowels: {vowel_count}, Consonants: {consonant_count}, Digits: {digit_count}, Specials: {special_count}")



# Q10

n = int(input("Enter number of rows (n): "))

for row in range(1, n + 1):
    for col in range(1, row + 1):
        if col % 3 == 0 and col % 5 == 0:
            print("Z", end=" ")
        elif col % 3 == 0:
            print("X", end=" ")
        elif col % 5 == 0:
            print("Y", end=" ")
        else:
            print(col, end=" ")
    print()  # Jumps to the next line



# Q11

for i in range(1, 6):
    username = input(f"Enter username {i}: ")
    
    length = len(username)
    first_letter = username[0] if length > 0 else ""
    
    digit_count = 0
    underscore_count = 0
    has_invalid_special = False
    
    for sym in username:
        if sym.isdigit():
            digit_count += 1
        elif sym == "_":
            underscore_count += 1
        elif not sym.isalnum():
            has_invalid_special = True
            
    # Classification logic
    if has_invalid_special or length == 0:
        print(f"'{username}' -> Invalid")
    elif length >= 8 and first_letter.isalpha() and digit_count >= 1 and underscore_count >= 1:
        print(f"'{username}' -> Valid")
    else:
        print(f"'{username}' -> Needs Improvement")