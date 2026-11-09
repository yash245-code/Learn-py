# First a heading about what the Program is for.
print("+" + "-"*40 + "+")
print(f"|{" ":>10}Bill and Tip Splitter{" ":<9}|")
print("+" + "-"*40 + "+")

# Step 1 : Take all the nessary inputs.
bill = float(input("Enter the total amount of bill (in rupees) : "))
tip = float(input("Enter the tip you want to give (in rupees) : "))
gst = float(input("Enter the GST (in % \"\") : "))
n = float(input("Enter the number of people : "))

# Check if the inputs are recived and converted.
print(bill, tip, gst, n, "\n")

# Processing :
tax = bill * gst / 100
total_bill = bill + (bill * gst / 100)
avg_bill = bill / n
avg_tax = tax / n

# Bill Heading Template and Bill Body
print("+" + "-"*55 + "+")
print(f"|\tBill : {bill:.2f}{" "*8}Tax/GST : {tax:.2f} \t\t|")
print("+" + "-"*55 + "+")
print(f"|\tIndividual Amount \t: \t{avg_bill:.2f} \t\t|")
print(f"|\tIndividual Tax  \t: \t{avg_tax:.2f} \t\t|")
print(f"|\tIndividual Total \t: \t{avg_bill+avg_tax:.2f} \t\t|")
print("+" + "-"*55 + "+")
print(f"|\tGrand Total  \t\t: \t{total_bill:.2f} \t|")
print("+" + "-"*55 + "+")
