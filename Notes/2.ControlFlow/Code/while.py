# While loop programs for better control flow

# All the important imports for any of the programs
from ast import While
import random


#1. Counting Numbers
i = 1
while i<=5:
    print("Count : ",i)
    i += 1

#2. Sum of digits
n = int(input("Enter any number : "))
total = 0
while n > 0:
    total += n % 10
    n //= 10
print("Sum of the digits : ",total)

#3. Reverse a number
n = int(input("Enter any number : "))
rev = 0
while n > 0 :
    rev = 10 * rev + n % 10
    n //= 10
print("The reverse is : ",rev)

#4. Password with limited attempts
attempts = 0
while attempts < 3:
    pwd = input("Password : ")
    if pwd == "user@123":
        print("Acess Granted !")
        break
    attempts += 1
    print(f"Wrong. {3 - attempts} attempts(s) left")

#5. Number guessing game
secret = random.randint(1, 20)
tries = 0
while True:
    guess = int(input("Guess (1-20): "))
    tries += 1
    if guess < secret:
       print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print(f"Correctly gussed in {tries} tries!")
        break

#6. Factorial
n = int(input("Enter a number : "))
fact, i = 1, 1
while i<=n:
    fact *= i
    i += 1
print(f"{n} = {fact}")

#7. Collatz Sequence
n = 27
steps = 0
while n != 1:
    n = n // 2 if n % 2 == 0 else 3 * n+ 1
    steps += 1
print("Reached 1 in ", steps, "steps")

#8. Palindrome
n = int(input("Enter a number : "))
original, rev = n, 0
while n>0 :
    rev = rev * 10 + n % 10
    n //= 10
print("Palindrome" if rev == original else "Not a Palindrome")

#9. Menu-Driven Program.
balance = 1000
while True :
    print("\n1. Check Balance 2. Deposit 3. Withdraw 4. Exit")
    choice = input("Choose: ")
    if choice == "1":
        print("Balance :", balance)
    elif choice == "2":
        balance += float(input("Amount : "))
    elif choice == "3" :
        amt = float(input("Amount : "))
        if amt <= balance:
            balance -= amt
        else :
            print("Insufficient Funds")
    elif choice == "4":
        print("Goodbye")
        break
    else:
        print("Invalid Choice")

#10. GCD using Euclid's algorithm and binary conversion
a, b = 48, 18
while b != 0:
    a, b = b, a % b
print("GCD = ",a)
n = 25
bits = ""
while n > 0:
    bits = str(n % 2) + bits
    n //= 2
print("Binarry of 25 = ",bits)
