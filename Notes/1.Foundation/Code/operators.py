#1. Arithmetic Operators
a, b = 4, 5
print(a+b, a-b, a*b)
print(a/b, a//b, a%b, a**b)

#2. Floor division and modulus with negatives
print(-17 // 5)                 # -4 ( Floors towards negative infinity )
print(-17 % 5)                  # 3 ( Result has the sign of the divisor )
print(17 // -5, 17 % -5)
print(divmod(17, 5))

#3. Power and roots
print(2 ** 10)
print(9 ** 0.5)                 # square root
print(27 ** 1/3)                # cube root(approx)
print(pow(2, 5, 7))             # (2**5) % 7

#4. Comparision and chaining
x = 7
print(x==7, x!=7, x>5, x<=6)
print(1 < x < 10)
print(len("apple"), len("banana"))
print("apple" < "banana")

#5. Logical operators and short-circuit
print(True and False, True or False, not True, not False)
print(0 or "default")
print("hi" and "there")
print(5 and 0)

#6. Augmented assignment
score=10
print(score)
score+=5
print(score)
score-=3
print(score)
score*=2
print(score)
score//=5
print(score)
score**=2
print(score)

#7. Bitwise Operator
a,b = 12, 10
print(a&b, a|b, a^b)
print(~a, a<<1, a>>2)
print(bin(a & b))

#8. is vs ==
a=[1, 2, 3]
b=[1, 2, 3]
c=a
print(a==b)                     # True (Have the same value)
print(a is b)                   # False (Different objects)
print(a is c)                   # True (Both point to the same object)

#9. Membership Operator
print("y" in "Yash".lower())
print(3 in [1, 2, 3], 5 not in [1, 2, 3])
print("name" in {"name": "Yash"})               # Checks Keys

#10. Precedence in a real use: even/odd and leap year
print(2 + 3 * 4 ** 2 )          # 50
print((2+3) * 4  ** 2)          # 80
n = 14
print("even" if  n % 2 == 0 else "odd")
year = 2028
print((year % 4 == 0 and year % 100 != 0 ) or year % 400 == 0)
