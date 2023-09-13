a = ["Black", "Brown", "Red", "Orange", "Yellow", "Green", "Blue", "Violet", "Grey", "White"]

# Tolerance
b = ["a", "a", "a", "a", "a", "Golden", "a", "a", "a", "a", "Silver", "a", "a", "a", "a", "a", "a", "a", "a", "a", "None"]

# input Color
c = a.index(input("Enter 1st Color : "))
d = a.index(input("Enter 2nd Color : "))
e = a.index(input("Enter 3rd Color : "))
f = b.index(input("Enter Tolerance : "))

# Process
g = int(((c*10)+d)*(10**(e)))
h = int(g*f)/100
i = (g+h)
j = (g-h)

# Output
k = (g+h)/1000
l = (g-h)/1000

# Score
print("____________Ω_____________")
print("Highest Score", i, "Ω")
print("Lowest Score", j, "Ω")

# Score KΩ
print("____________KΩ____________")
print("Highest Score", k, "KΩ")
print("Lowest Score", l, "KΩ")