#2.2. for Loop

#1. range() basics
for i in range(5):
    print(i, end=" ")
print()
for i in range(1, 6):
    print(i, end=" ")
print()

#2. Step and Reverse
for i in range(0, 21, 5):
    print(i, end=" ")
print()
for i in range(10, 0, -2):
    print(i, end=" ")
print()

#3. Looping over a string
for ch in "Python":
    print(ch, end="-")
print()
for fruit in ["apple", "banana", "mango"]:
    print(fruit.upper())
print()

#4. Sum and average of 1 to n
n = int(input("Enter a number : "))
sum = 0
for i in range(1, n):
    sum = sum + i;
print(f"The sum of all n numbers is : {sum}")
print(f"The average of all the numbers is : {sum/n}")
