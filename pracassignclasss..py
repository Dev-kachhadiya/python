operation=int(input("Enter the number of operation you want to do: \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division :"))

if operation==1 or operation==2 or operation==3 or operation == 4:
     
    number1 = int(input("Enter first number: "))

    number2 = int(input("Enter second number: "))

    if operation == 1:
        print(f"Addition:{number1+number2}")

    elif operation == 2:
          print(f"Subtraction: {number1-number2}")

    elif operation == 3:
          print(f"Multiplication: {number1*number2}")

    elif operation == 4:
          print(f"Division: {number1/number2}")

else:
  print("Try again")


    