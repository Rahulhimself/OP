bill = float(input("whats was the total bill :"))
tip = int(input("how much tip would you like to give 10 or 15 0r 20:"))
contri = int(input("how many are contributing :"))
final_bill = "{:.2f}".format(((bill * tip / 100 ) + bill) / contri)
print(f"the total amount each should pay is : {final_bill}")


