#2.2. for Loop
'''
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

#5. Multiplication table
num = int(input("Enter any number : "))
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")
print()

#6. Factorial of any number
num = int(input("Enter any number : "))
fact = 1
for i in range(2, num+1):
    fact *= i
print(f"The factorial of num {num} is : {fact}")

#7. enumerate() and zip()
names = ["Yash", "Harsh", "Sagar"]
marks = [90, 95, 100]
for index, name in enumerate(names, start=1):
    print(index, name)
for name, marks in zip(names, marks):
    print(f"{name} : {marks  }")

#8. Count vowels in a string.
text = input("Enter text : ").lower()
count = 0
for ch in text:
    if ch in "aeiou":
        count += 1
print(f"The number of vowels in the string you entered are : {count}")

#9. Fibonacci Series.
n = int(input("How many terms in the fibonacci series : "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a+b
print()
'''
#10. Even numbers, sum and manual max of a list
nums = [12, 4, 5, 6, 3, 2]
evens = []
biggest = nums[0]
for x in nums:
    if x % 2 == 0:
        evens.append(x)
    if x > biggest:
        biggest = max(biggest, x)
print("Evens : ", evens)
print("Sums : ", sum(nums), "| Max : ",biggest)
