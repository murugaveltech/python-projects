# pyhton program to interchange first and last elements in a list

l = [1, 2, 3, 4, 5, 6]
t = l[0]
l[0] = l[len(l) - 1]


l[len(l) - 1] = t
print(l)

l = ["Hi", "Hello", "Good", "morning", "something"]
t = l[0]
l[0] = l[len(l) - 1]

l[len(l) - 1] = t
print(l)


# python program to swap two elements in a list

swap = [23, 43, 12, 89, 90, 34]
print(swap)

pos1, pos2 = 2, 5

swap[pos1], swap[pos2] = swap[pos2], swap[pos1]

print(list)


# minimum and maximum of two numbers in python


def num(a, b):
    if a >= b:
        return a
    else:
        return b


a = int(input("Enter first num :"))
b = int(input("Enter second num :"))
print(num(a, b))


print(max(4, 12, 43.3, 19, 100))
print(min(4, 12, 43.3, 19, 100))

# python program to print negative numbers in a range

for num in range(-14, 8):

    if num < 0:
        print(num)


number = [12, 34, -29, 30, -54, -32, 23, -54, 21]

for li in number:
    if li < 0:
        print(li)


# Find sum and average of list in python

L = [4, 5, 1, 2, 9, 7, 10, 8]

count = sum(L)

avg = count / len(L)

print("sum = ", count)
print("avg is", avg)


# remove empty list from list

mylist = [12, 32, [], 43, 12, [], 65, 89, [], 56]

print("the original list " + str(mylist))

var = list(filter(None, mylist))
print("empty list filter " + str(var))
