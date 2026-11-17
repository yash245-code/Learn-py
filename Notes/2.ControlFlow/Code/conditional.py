# Python file ot check all my knowledge of Conditional Statements

#1. Simple if
temperature = 38
if temperature > 35:
    print("It is hot Today !")
print("Program finished")

#2. if-else : Voting eligibility
age = int(input("Enter your age : "))
if age >= 18:
    print("You can vote.")
else:
    print(f"You canot vote after {18 - age} more year(s)")

#3. if-elif-else : grade calculator
marks = int(input("Enter marks (0-100) : "))
if marks>=90:
    print("A+")
elif marks>=80:
    print("A")
elif marks>=70:
    print("B")
elif marks>=40:
    print("C")
else :
    grade = "FAIL"
    print("Grade :", grade)

#4.Nested if: simple logic check
username = input("Username : ")
passoword = input("Password : ")
if username == "admin":
    if passoword == "admin@123":
        print("Welcome! Admin")
    else:
        print("Wrong Passoword")
else:
    print("Unknown User")

#5. Ternary (Conditional Expression)
n = int(input("Enter a number : "))
parity = "even" if n%2 == 0 else "odd"
print(n, "is", parity)
sign="positive" if n>0 else "Negative" if n<0 else "zero"
print(n, "is", sign)

#6. Largest of the three numbers
a, b, c = 12, 32, 12
if a>=b and a>=c:
    largest = a
elif b>=a and b>=c:
    largest = b
else:
    largest = c
print("The largest number is : ",largest)
print("Using max() : ", max(a, b, c))

#7. Leap Year Checker
year = int(input("Enter a year! : "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

#8. Truthness in conditions
name = ""
items = [3, 5]
if not name:
    print("Name is Empty")
if items:
    print("Items found:", items)
value = None
if value is None:
    print("No value set")

#9. match case :
day = int(input("Day number (1-7): "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3 | 4 | 5:
        print("Midweek")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Invalid Day")

#10. Calculator using if-elif
a = float(input("First Number : "))
op = input("Operator (+, -, /, *) : ")
b = float(input("Second Number : "))
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a/b  if b!= 0 else "Cannot divide by zero")
else:
    print("Invalid Sign.")
