setc1 = {"Beige" , "Green" , "Yellow" , "Red" , "Blue" , "Purple"}
setc2 = {"Brown" , "Green" , "Pink" , "Orange" , "Blue" , "Purple"}
setc3 = {"Brown" , "Teal" , "Pink" , "Lavender" , "Blue" , "Purple"}
setc4 = {"Brown" , "Teal" , "Pink" , "Lavender" , "Silver" , "Purple"}
setc5 = {"Brown" , "Teal" , "Pink" , "Lavender" , "Silver" , "Purple","Maroon"}


print("Original Sets :")

print(setc1)
print(setc2)
print(setc3)
print(setc4)
print(setc5)

setA = setc1.union(setc2)
setB = setc3.union(setc4)
setC = setc4.union(setc5)

print("\n Union Of Setc1 and Setc2 :")

print(setA)

print("\n Union Of Setc3 and Setc4 :")

print(setB)
print("\n Union Of Setc4 and Setc5 :")

print(setC)