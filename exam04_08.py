price = 12_345.00
qty = int(input("Enter Quantity Product : "))
print()
total = price * qty
print("Total Price : ",format(total,',.2f'))
vat = total * 0.07
print("Vat (7%) : ",format(vat,',.2f'))
allTotal = total + vat
print("All Total : ",format(allTotal,',.2f'))
print("ALL Total : ",format(allTotal,'#>20,.2f'))