# Two number in (a and b). find c.

a = int(input("Enter first number :"))
b = int(input("Enter second number :"))

c = a + b
print("The total is :" + str(c))


# print the number of days in the month corresponding to that number

month = int(input("Enter month num :"))
year = int(input("Enter year num :"))

mon = [1, 3, 5, 7, 8, 10, 12]
if month in mon:
    print("Number of days is 31")
elif (month == 2) and ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)):
    print("Number of days is 29")
elif month == 2:
    print("Feb month of days is 28")
else:
    print("Number of days is 30")


# leap year simple calculated
year = int(input("Enter year :"))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, "is the leap year")
else:
    print(year, "is the not leap year")
