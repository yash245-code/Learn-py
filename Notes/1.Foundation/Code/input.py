'''#1. Input returns a string
name = input("Enter your name: ")
print("Hello ", name)
print(type(name))

#2. Add two integers
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
print(f"The sum of {num1} and {num2} is : ", num1 + num2)

#3. Average of 3 numbers (float input)
m1 =  float(input("Enter first number : "))
m2 =  float(input("Enter second number : "))
m3 =  float(input("Enter third number : "))
print(f"Average : {(m1+m2+m3)/3:.2f}")

#4. Type Casting
print(int("42")+ 3)
print(int(3.99))
print(float("2.5")* 2)
print(str(100) + " marks")
print(bool(""), bool("0"))
print(list("abc"), tuple([1, 2]), set([1, 1, 3]))

#5. Safe conversion with try/except
text = input("Enter a number : ")
try:
    num = float(text)
    print("You entered : ", num)
except ValueError:
    print("That is not a valid number.")

#6. Multiple values on one line
x, y = map(int, input("Enter two number:").split())
print("Product = ", x*y)
nums = list(map(int, input("Enter many numbers : ").split()))
print(nums, "Total = ", sum(nums))

#7. Formatting output with f-strings
price = 1234.5678
n = 7
print(f"{price:.2f}")
print(f"{price:,.1f}")
print(f"|{n:>5}| |{n:<5}| |{n:^5}| |{n:05d}|")
print(f"{0.256:.1%}")

#8. Simple interest calculator
p = float(input("Principal : "))
r = float(input("Rate (% per year : "))
t = float(input("Time (years) : "))
si = p * r * t / 100
print(f"Simple Intrest : {si:.2f}")
print(f"Total Amount : {p + si}")

#9. Temperature Convertor
c = float(input("Temperature in Celsius: "))
f = c * 9/5 +32
k = c + 273.15
print(f"{c}°C = {f:.1f}°F = {k:.2f}K")          '''

#10. Mini Bill Generator
item = input("Item name : ")
qty = int(input("Quantity : "))
rate = float(input("Rate per unit : "))
subtotal = qty * rate
gst = subtotal * 0.18
print("-" * 30)
print(f"{item:<12}{qty:>4} x {rate:>9.2f}")
print(f"{'Subtotal':<18}{subtotal:>10.2f}")
print(f"{'GST (18%)':<18}{gst:>10.2f}")
print(f"{'Total':<18}{subtotal + gst:>10.2f}")
print("-" * 30)
