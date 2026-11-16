# Python file ot check all my knowledge of Conditional Statements

# 1. Simple if
temperature = 38
if temperature > 35:
    print("It is hot Today !")
print("Program finished")

# 2. if-else : Voting eligibility
age = int(input("Enter your age : "))
if age >= 18:
    print("You can vote.")
else:
    print(f"You canot vote after {18 - age} more year(s)")

# 3. if-elif-else : grade calculator
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

# 4.Nested if: simple logic check
username = input("Username : ")
passoword = input("Password : ")
if username == "admin":
    if passoword == "admin@123":
        print("Welcome! Admin")
    else:
        print("Wrong Passoword")
else:
    print("Unknown User")

# 5. Ternary (Conditional Expression)
n = int(input("Enter a number : "))
parity = "even" if n%10 == 0 else "odd"
print(n, "is", parity)
sign="positive" if n>0 else "Negative" if n<0 else "zero"
print(n, "is", sign)
