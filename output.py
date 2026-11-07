#This is my efforts towards learning python by doing something everyday hope i will be consistent and make myself proud.
#               DATE : 7/11/2026


#1 Hello World --
print("Hello World!")

#2  Printing multiple values --
print("Yash", "is", "washed")
print("Age: ", 21, "Marks:", 8.35)

#3 Sep Parameter --
print("07", "11", "2026", sep="-")
print("yash", "gmail.com", sep="@")

#4 End Parameter --
print("Loading", end="... ")
print("done")
print("A", end=" ")
print("B", end=" ")
print("C")

#5 Escape Sequence --
print("Name:\t Yash \n City:\t Haldwani")
print("Path: C\\users\\yash")

#6 Quotes inside string --
print("It's a nice day")
print('She said "YES"')
print("He said \"Bye\"")

#7 Triple-quoted multi line commment --
print('''Line 1
    Line 2
    Line 3''')

#8 Repeating string to draw  --
print("*" * 10)
print("-" * 10)
print("+" * 10)

#9 A simple bannder using f-strings and comments --
name = "Yash"
print("+" + "-"*16 + "+")
print(f"| Hello, {name:<8}|")
print("+" + "-"*16 + "+")

#10 Raw string and docstring --
"""This is a docstring-style comment.
It can span many lines."""
print(r"C:\new\table")
print("C:\new\table")
