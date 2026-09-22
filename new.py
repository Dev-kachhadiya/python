
# a,b=map(int,input("Enter two numbers:").split())

# print(f"first_num:{a}, second_num: {b}")



# a,b=input("enter two numbers:").split()

# print same as 1st


# a,b=map(int,input("Enter two numbers:").split()[:2])

# print(f"first_num:{a}, second_num: {b}")


# print("Hello" , end=" " )
# print("World")


# result=35

# if result>30:
#    print("pass")


# number=int(input("enter a number:"))

# if number%2==0:
#    print("even  number")

#    if number%2==1:
#        print("odd number")

# age=int(input("Enter age").split()[0])
# gender=input("enter your gender: " )
# gender=gender.lower().strip()
# print(age,gender)

# if age>=18:
#     if gender=="female":
#        print("seat is available for you!")

#     if gender!="female":
#        print("seat is not available for you!") 


# age=16

# if age >= 18:
#     print("you are an adult")
# else:
#     print("you are not an adult")

# gmail="devkachhadiya11@gmail.com"
# password=12345

# if gmail=="devkachhadiya11@gmail.com":
#    if password==12345:
#        print("logged in")
#    else:    
#        print("incorrect password")

# else:
#    print("gmail incorrect")


# str=input("Enter a String:").strip()
# str2=""
# length=len(str)

# for element in range (length-1,-1,-1):

#     str2=str2+str[element]

# if str==str2:
#     print("equal")
# else:
#     print(not equal)


# for i in range(5):
#     for j in range(4):
#          print("*" , end="")
#     print()


# for i in range(0,4):
#     for j in range(0, i + 1):
#          print("*" , end="")
#     print()


# for i in range(4,0,-1):
#     for j in range( i ):
#          print("*" , end="")
#     print()

# number=int(input("Enter a Number:"))

# for i in range(1,number):
#     for j in range(1,i+1):
#          print(j , end="")
#     print()         
   
  
# for i in range(1,6):
#      for j in range(1,5 - i):
#          print(" ",end="")
#      for k in range(1,i +1  ):
#          print("*",end="")
#      print()



# for i in range(0,6):
#    print(" "*(5-i)+"*" * i)

# num=int(input("Enter a row value:"))
for i  in range (0,5):
     for j in range(i):
          print("",end="")
     for k in range(0,5-i):
          print("*",end="")
     print()