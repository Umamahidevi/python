
#1
# Create two variables a = 10 and b = 6. Print the result of a & b.
a = 10
b = 6

print("Result:", a & b)
#2
# Create two variables x = 12 and y = 5. Print the result of x | y.
x = 12
y = 5

print("Result:", x | y)
#3
# Create a variable num = 8. Print the result of ~num.
num = 8

print("Result:", ~num)

#4
#Create two variables a = 15 and b = 9. Print the result of a ^ b.
a = 15
b = 9

print("Result:", a ^ b)

#5
#Create a variable num = 7. Perform left shift by 2 and print the result.
num = 7

print("Result:", num << 2)

#6
#Create a variable num = 20. Perform right shift by 1 and print the result.
num = 20

print("Result:", num >> 1)

#7
#Take two numbers from user input and print AND result.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("AND Result:", a & b)

#8
# Take two numbers from user input and print XOR result in python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("XOR Result:", a ^ b)

#9
# Create a string "hi" and print it 4 times using replication.
text = "hi"

print(text * 4)

#10
# Create a string "python" and print it 3 times.
text = "python"

print(text * 3)

#11 
# Create two strings "super" and "man" and combine them using + operator.
a = "super"
b = "man"

print(a + b)

#12
# Create three strings "hello", " ", "world" and print "hello world".
a = "hello"
b = " "
c = "world"

print(a + b + c)

#13
# Take a name from user input and print it 5 times. 
name = input("Enter your name: ")

print(name * 5)

# 14. 
# Take two strings from user input and concatenate them. with outputs in python
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

print("Combined String:", str1 + str2)

#15.
# Take a name from user input and print its data type.
name = input("Enter your name: ")

print("Data type:", type(name))

#16.
# Take age from user input and convert it into integer.
age = int(input("Enter your age: "))
print("Age:", age)

print("Data type:", type(age))

#17.
# Take two numbers from user input and print their sum.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)

#18.
#Take two marks from user input and print their average.
m1 = int(input("Enter first mark: "))
m2 = int(input("Enter second mark: "))
avg = (m1 + m2) / 2

print("Average:", avg)

#19.
# Take two numbers from user input and print 3*a*2 + b - 2.
a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
result = 3*a*2 + b - 2

print("Result:", result)


#20.Take a number from user input and print its data type before and after type casting.Unit Digit Tasks (21–25)
num = input("Enter a number: ")
print("Before casting:", type(num))

num = int(num)
print("After casting:", type(num))

#21.
# Take a number as string input and print the last digit.
num = input("Enter number: ")

print("Last digit:", num[-1])

#22.
# Take a number and print the unit digit using % operator.
num = int(input("Enter number: "))

print("Unit digit:", num % 10)

#23.
# Take a number and remove the last digit using // operator.
num = int(input("Enter number: "))

print("Number after removing last digit:", num // 10)

#24.
# Take a number and print the second last digit.
num = int(input("Enter number: "))

print("Second last digit:", (num // 10) % 10)

#25.
# Take a 5 digit number and print its last digit.If Statement Tasks (26–30)
num = int(input("Enter 5 digit number: "))

print("Last digit:", num % 10)

#26.
# Create a program that checks if 10 ≥ 5 and prints a message.
if 10 >= 5:
    print("10 is greater than or equal to 5")

#27.
# Take a number from user input and check if it is greater than 50.
num = int(input("Enter number: "))

if num > 50:
    print("Number is greater than 50")

#28.
# Take age from user input and check if age ≥ 18.
age = int(input("Enter age: "))

if age >= 18:
    print("Eligible to vote")

#29.
# Take a number and check if it is greater than 100.
num = int(input("Enter number: "))

if num > 100:
    print("Number is greater than 100")

#30.
#Take a number and check if number ≥ 0.If-Else Tasks (31–34)
num = int(input("Enter number: "))

if num >= 0:
    print("Number is non-negative")

#31.
# Take a number and check if it is even or odd.
num = int(input("Enter number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

#32.Take marks from user input and check if pass or fail (pass ≥ 35).
marks = int(input("Enter marks: "))

if marks >= 35:
    print("Pass")
else:
    print("Fail")

#33.Take a number and check if it is positive or negative.
num = int(input("Enter number: "))

if num > 0:
    print("Positive number")
else:
    print("Negative number")

#34.Take a number and check if it is greater than 10 or not.Nested If Tasks (35–37)
num = int(input("Enter number: "))

if num > 10:
    print("Number is greater than 10")
else:
    print("Number is not greater than 10")

#35.Create a program for job eligibility:
#Conditions
#Age ≥ 18
#Height ≥ 160
#Weight ≥ 60
#Print selected or rejected.
age = int(input("Enter age: "))
height = int(input("Enter height: "))
weight = int(input("Enter weight: "))

if age >= 18:
    if height >= 160:
        if weight >= 60:
            print("Selected")
        else:
            print("Rejected")
    else:
        print("Rejected")
else:
    print("Rejected")

#36.
#Create a college admission program:
#Conditions
#Marks ≥ 60
#Age ≥ 17
marks = int(input("Enter marks: "))
age = int(input("Enter age: "))

if marks >= 60:
    if age >= 17:
        print("Admission Granted")
    else:
        print("Age not eligible")
else:
    print("Marks not eligible")

#37.
#Create a sports selection program:
#Conditions
#Age ≥ 16
#Height ≥ 150
#Weight ≥ 50
#Match Statement Tasks (38–40)
age = int(input("Enter age: "))
height = int(input("Enter height: "))
weight = int(input("Enter weight: "))

if age >= 16:
    if height >= 150:
        if weight >= 50:
            print("Selected for sports")
        else:
            print("Not selected")
    else:
        print("Not selected")
else:
    print("Not selected")

#38.
#Take a number (1-7) and print day name using match.
day = int(input("Enter number (1-7): "))

match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")

#39.
#Take a number (1-3) and print:
#1 → Red
#2 → Blue
#3 → Green
num = int(input("Enter number (1-3): "))

match num:
    case 1:
        print("Red")
    case 2:
        print("Blue")
    case 3:
        print("Green")

#40.
# Take a number (1-4) and print:
#1 → Apple
#2 → Mango
#3 → Orange
#4 → Banana
num = int(input("Enter number (1-4): "))

match num:
    case 1:
        print("Apple")
    case 2:
        print("Mango")
    case 3:
        print("Orange")
    case 4:
        print("Banana")