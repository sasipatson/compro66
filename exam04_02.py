# Program name : exam04_02 #
n1 = int (input("Enter Value Number 1 : "))
n2 = int (input("Enter Value Number 2 : "))
n3 = int (input("Enter Value Number 3 : "))
MinValue = min(n1,n2,n3)
MaxValue = max(n1,n2,n3)

print()
print("Your Enter Number : ",n1,n2,n3)
print("Maximum Value : ",MaxValue)
print("Minimum Value : ",MinValue)
print("Averrage Value : ",round(sum((n1,n2,n3))/3,2))