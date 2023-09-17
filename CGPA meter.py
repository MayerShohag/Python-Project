first = float(input("Enter 1st Semester Result : "))
second = float(input("Enter 2nd Semester Result : "))
third = float(input("Enter 3rd Semester Result : "))
forth = float(input("Enter 4th Semester Result : "))
fifth = float(input("Enter 5th Semester Result : "))
sixth = float(input("Enter 6th Semester Result : "))
seventh = float(input("Enter 7th Semester Result : "))
eighth = float(input("Enter 8th Semester Result : "))

a = float((first*5)/100) # semester %
b = float((second*5)/100) # semester %
c = float((third*10)/100) # semester %
d = float((forth*10)/100) # semester %
e = float((fifth*20)/100) # semester %
f = float((sixth*20)/100) # semester %
g = float((seventh*20)/100) # semester %
h = float((eighth*10)/100) # semester %

x = (a+b+c+d+e+f+g+h) # average semester
print("CGPA is : %.2f" % x)
