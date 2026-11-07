# VARIABLES : Some important properties and uses of different datatypes in python.

#1. Int : Unlimited size and readable literals
big = 2 * 100
print(big)
print(1_000_000 + 1)
print(type(big))

#2. Float and Precision
print(0.1 + 0.2)                # 0.30000000000000004
print(round(0.1 + 0.2), 2)      # 0.3
print(2e3, float)           # 2000.0 <class 'float'>

#3. Complex Numbers
z = 3 + 4j
print(z.real, z.imag)
print(abs(z))                   # Magnitude 5.0
print(z * (1 - 2j))

#4. Bool is a subclass of int
print(True + True)
print(int(True), int(False))
print(isinstance(True, int))

#5. str basics : indexing and immutability
s = "Python"
print(s[0], s[-1], len(s))
try:
    s[0] = 'J'
except TypeError as e:
    print("Error :", e)

#6. None the absence of value
result = None
print(result, type(result))
print(result is None)

#7. type() vs isinstance()
x = 3.5
print(type(x))
print(isinstance(x, float))
print(isinstance(x, (int, float)))  # Check against several types

#8. Number System
n = 25
print(bin(n), oct(n), hex(n))
print(0b101, 0o5, 0x5)
print(int("11001", 2), int("47", 8), int("ff", 16))

#9. Truthy and Falsy values
values = [0, 1, "", "hi", [], [0], None, 0.0, {}, " "]
for v in values:
    print(repr(v), "->", bool(v))

#10. Mutable vs immutable (preview)
nums = [1, 2, 3]
nums[0] = 99
print(nums)
t = (1, 2, 3)
try:
    t[0]
except TypeError as e:
    print("Tuple error:", e)
print(type(nums), type(t), type({1, 2}), type({"a": 1}))
