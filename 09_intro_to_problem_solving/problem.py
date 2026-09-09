#Q1
num1=int(input("Enter a number:"))

if num1 > 0:
    print("Positive")
elif num1< 0:
    print("Negative")
elif num1 == 0:
    print("Zero")

else:
    print("Not a number")
#Q2

num2=int(input("Enter a Number:"))

if num2 > 0 and num2%2==0:
    print("Positive Even")
elif num2 >0 and num2%2!=0:
    print("Positive odd")
elif num2<0 and num2%2==0:
    print("Negative Even")
elif num2<0 and num2%2!=0:
    print("Negative Odd")
elif num2==0:
    print("Zero")
else:
    print("Invalid Number")

n1=int(input("Enter First Number:"))
n2=int(input("Enter Second Number:"))

if n1 > n2:
    print(n1)
elif n2 > n1:
    print(n2)
elif n1 == n2:
    print("Both are equal")
else:
    print("Undefined number entered")

#Q4

nu1=int(input("Enter First Number:"))
nu2=int(input("Enter Second Number:"))
nu3=int(input("Enter Third Number:"))

if nu1<nu2 and nu1<nu3:
    print(nu1)
elif nu2<nu1 and nu2<nu3:
    print(nu2)
elif nu3<nu1 and nu3 < nu2:
    print(nu3)
else:
    print("Not a number entered")

#Q5

nb1=int(input("Enter First Number:"))
nb2=int(input("Enter Second Number:"))
nb3=int(input("Enter Third Number:"))

if nb1>nb2 and nb1>nb3:
    print(nb1)
elif nb2>nb1 and nb2>nb3:
    print(nb2)
elif nb3<nb1 and nb3 < nb2:
    print(nb3)
else:
    print("Not a number entered") 

#Q6

num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
elif num % 5 == 0:
    print("Divisible only by 5")
elif num % 11 == 0:
    print("Divisible only by 11")
else:
    print("Divisible by neither")

#Q7

number = int(input("Enter a Number:"))

if number % 3 == 0 and number % 7 == 0:
    print("Divisible by both")
elif number % 3 == 0 :
    print("Divisible by only 3")
elif number % 7 == 0:
    print("Divisible by only 7")
else :
    print("Divisible by neither")

#Q8

marks=int(input("Enter your marks:"))

if marks<0 or marks>100:
    print("Invalid marks")

elif marks>=40:
    print("Pass")
elif marks<40:
    print("Fail")
else :
    print("Entered marks are not integer type")

#Q9
mark=int(input("Enter your marks:"))

if mark>=90:
    print("A")
elif mark>=80:
    print("B")
elif mark>=70:
    print("C")
elif mark>=60:
    print("D")
elif mark>=40:
    print("E")
else:
    print("FAIL")

#Q10

age=int(input("Enter your Age:"))

if age<0:
    print("Invalid Age")
elif age<18:
    print("Cannot Vote")
elif age>=18:
    print("Can vote")
elif age>=120:
    print("Unrealistic age entered")

#Q11

year=int(input("Enter a year:"))

if (year % 400 == 0) or (year % 4 == 0 and not year % 100 == 0):
    print("It is a leap Year!!!!")

else:
    print("It's not a leap Year.")

#Q12

#Q13
inn=input("Enter alphabets:").strip().lower()

if inn == "a" or inn == "e" or inn=="o" or inn=="u" or inn=="i":
    print("It's a vowel")
elif inn=="b" or inn=="c" or inn=="d" or inn=="f" or inn=="g" or inn=="h" or inn=="j" or inn=="k" or inn=="l" or inn=="m" or inn=="n" or inn=="p" or inn=="q" or inn=="r" or inn=="s" or inn=="t" or inn=="v" or inn=="w" or inn=="x" or inn=="y" or inn=="z":
    print("It's a consonant")
else:
    print("Invalid Input")

#Q14

cost=int(input("Enter the cost of Product:"))
sell=int(input("Enter the selling price of product:"))

if (cost-sell)>0:
    print(f"It's a Loss of {cost-sell}")
elif (sell-cost)>0:
    print(f"It's a Profit of {sell-cost}")
elif (sell-cost)==0:
    print("No profit and no loss")
else:
    print("Invalid Input")

#Q15

Cost=int(input("Enter the cost of your product:"))
Sell=int(input("Now Selling price of your product:"))
profit=Sell-Cost
loss=Cost-Sell

if Cost<=0:
    print("Invalid Cost Price")
elif (Sell-Cost)>0:
    print(f"It's a profit of {profit} and it's percentage is {(profit/Cost)*100}")
elif (Cost-Sell)>0:
    print(f"It's a loss of {loss} and it's percentage is {(loss/Cost)*100}")
else:
    print("Don't Try to play a game with me")

#Q16 

bill=int(input("Enter the units of your bill:"))

if bill<=100:
    print(f"Your toatl bill is ₹{bill*5}")
elif bill<=200:
    print(f"Your total of bill is ₹{(100*5)+((bill-100)*7)}")
elif bill>200:
    print(f"Your total of bill is ₹{(1200)+((bill-200)*10)}")

#Q17
fnum=int(input("Enter first number:"))
snum=int(input("Enter second number:"))
op=int(input("Enter 1 for Addition\nEnter 2 for Substraction\nEnter 3 for Multiplication\nEnter 4 for Division:"))
if snum==0:
    print("Second Number cannot be zero")
elif op==1:
    print(f"Addition is {fnum+snum}")
elif op==2:
    print(f"Substraction is {fnum-snum}")
elif op==3:
    print(f"Multiplication is {fnum*snum}")
elif op==4:
    print(f"Division is {fnum/snum}")
else:
    print(f"Invalid input")


#Q18
t=int(input("Enter temperature in celsius:"))

if t<0:
    print("freezing")
elif t<=15:
    print("Very cold")
elif t<=25:
    print("Cold")
elif t<=35:
    print("Normal")
elif t>35:
    print("Hot")

#Q19
N=int(input("Enter a number:"))

if N<0:
    print("It's a negative number")
elif N<=10:
    print("Number is in betweem 0-10")
elif N<=50:
    print("Number is in betweem 11-50")
elif N<=100:
    print("Number is in between 51-100")
elif N>100:
    print("Number is above 100")

# #Q20

A=int(input("Enter the length of 1st side of triangle:"))
B=int(input("Enter the length of 2nd side of triangle:"))
C=int(input("Enter the length of 3rd side of triangle:"))

if (A+B>C) and (A+C>B) and (B+C>A):
    print("These lengths can form a Valid Triangle")
else:
    print("These lengths can't form a Valid Triangle")

#Q21
A=int(input("Enter the length of 1st side of triangle:"))
B=int(input("Enter the length of 2nd side of triangle:"))
C=int(input("Enter the length of 3rd side of triangle:"))


if (A+B>C) and (A+C>B) and (B+C>A):
    print("These lengths can form a Valid Triangle")
elif A+B<C or A+C<B or B+C<A:
    print("These lengths can't form a Valid Triangle")
elif A==B and B==C and A==C:
    print("It's a Equilateral triangle")
elif A==B and B!=C:
    print("It's a Isosceles Triangle")
elif B==C and A!=B:
    print("It's a Isosceles Triangle")
elif A==C and C!=B:
    print("It's a Isosceles")
elif A!=B and B!=C and A!=C:
    print("It's an Scalene Triangle")
 

#Q22

acc=int(input("Enter Account Balance:"))
wid=int(input("Enter The Withdrawal Amount:"))

if wid<=0:
    print("Withdrawal amount must be greater than 0")
elif not wid%100==0:
    print("Withdrawal amount must be in multiple of 100")
elif wid>acc:
    print("Withdrawal amount cannot be greater than account balance")
elif (acc-wid)<500:
    print("Withdrawal Unsuccesfull, After withdrawal atleast ₹500 must remain in Account")
else :
    print(f"Withdrawal Succesful\nRemaining balance: {acc-wid} ")

#Q23
use=input("Enter your username:")
pas=input("Enter your Password:")

if use!="admin":
    print("User not found")
elif pas!="python123":
    print("Wrong Password")
elif use=="admin" and pas=="python123":
    print("Login Succesful")

#Q24
pur=int(input("Enter the purchase amount:"))
di=(pur)-(pur*5/100)
dis=(pur)-(pur*10/100)
disc=(pur)-(pur*15/100)
discount=(pur)-(pur*20/100)

if pur<500:
    print(f"Original Amount:{pur}\nDiscount Percentage 0%\nDiscount Amount 0₹\nFinal Amount {pur}")
elif pur<1000:
    print(f"Original Amount:{pur}\nDiscount Percentage 5%\nDiscount Amount {pur*5/100}\nFinal Amount {di}")
elif pur<2000:
    print(f"Original Amount:{pur}\nDiscount Percentage 10%\nDiscount Amount {pur*10/100}₹\nFinal Amount {dis}")
elif pur<5000:
    print(f"Original Amount:{pur}\nDiscount Percentage 15%\nDiscount Amount {pur*15/100}₹\nFinal Amount {disc}")
elif pur>5000:
    print(f"Original Amount:{pur}\nDiscount Percentage 20%\nDiscount Amount {pur*20/100}₹\nFinal Amount {discount}")

#Q25
m=int(input("Enter your Physics marks:"))
ma=int(input("Enter your chemistry marks:"))
mar=int(input("Enter your MATHEMATICS marks:"))

if m<0 or m>100 or ma<0 or ma>100 or mar<0 or mar>100:
    print("Inappropriate marks please re-enter it!")
elif m<35 or ma<35 or mar<35:
    print("Result: Fail")
elif m>=35 and ma>=35 and mar>=35:
    print("Result: Pass")
    print(f"Your Average marks is {(m+ma+mar)/3}")
    if ((m+ma+mar)/3)>=75:
        print("Distinction")
    elif ((m+ma+mar)/3)>=60:
        print("First Class")
    elif ((m+ma+mar)/3)>=50:
        print("Second Class")
    elif ((m+ma+mar)/3)>=35:
        print("Pass")