# School report card generator

# Print the Beautifull Heading
print("+" + "-"*50 + "+")
print(f"|{"Report Card Generator":^50}|")
print("+" + "-"*50 + "+")
print(f"{"Note : 5 Subjects Required !":^52} \n")

# Take all the important inputs (Student's details & marks for all 5 subjects)
name = input("Enter your name : ")
fname = input("Enter your father's name : ")
std, sec = input("Enter your class and section (class section): ").split()
std = int(std)
rno = int(input("Enter your roll number : "))
'''

print(name, type(name), fname, type(fname), std, type(std), sec, type(sec), rno, type(rno) )


fullm = float(input("Enter full marks of one subject : "))
sub1 = input("\nEnter the name of first subject : ")
m1 = float(input(f"Enter marks for {sub1} : "))
sub2 = input("Enter the name of second subject : ")
m2 = float(input(f"Enter marks for {sub2} : "))
sub3 = input("Enter the name of third subject : ")
m3 = float(input(f"Enter marks for {sub3} : "))
sub4 = input("Enter the name of fourth subject : ")
m4 = float(input(f"Enter marks for {sub4} : "))
sub5 = input("Enter the name of fifth subject : ")
m5 = float(input(f"Enter marks for {sub5} : "))

# Process all the input :
tm = m1 + m2 + m3 + m4 + m5
cgpa = tm / 500
p = cgpa * 100
'''

# Build a clean template for the report card.

print("+" + "-"*100 + "+")
print(f"|{"Annual Report Card":^100}|")
print("+" + "-"*100 + "+")
print(f"|{"Student Details :":^100}|\n|{" "*100}|")

left1 = f"Student's Name : {name}"
right1 = f"Father's Name : {fname}"
left2 = f"Class : {std}{sec}"
right2 = f"Roll-No : {rno}"
print(f"| {" "*18}{left1:<40}{right1:<40} |")
print(f"| {" "*18}{left2:<40}{right2:<40} |")
print("+" + "-"*100 + "+")

print("+" + "-"*100 + "+")
head = f"|{"S.No":^6}|{"Subject":^25}|{"Grade":^15}|{"Marks":^15}|"
print(f"|{head:^100}|")
#for i in range(1, 6):
    #print(f"|{i:^5}{}|")
print("+" + "-"*100 + "+")
