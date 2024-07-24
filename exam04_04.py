import math

fnum = float(input("Enter Float Number : "))

print()
print("Ceil Number : ",math.ceil(fnum))
print("Floor Number : ",math.floor(fnum))
print("Sqrt Number : ",math.sqrt(fnum))
print("Trunc Number : ",math.trunc(fnum))

num = math.trunc(fnum)
print("Degree Angle : ",num)
print("Radians Angle : ",math.radians(num))
print("sin : ",math.sin(math.radians(num)))
print("cos : ",math.cos(math.radians(num)))
print("tan : ",math.tan(math.radians(num)))