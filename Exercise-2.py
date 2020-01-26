id = int(input("Type in an 8-digit ID number to check its validity: "))
print(" ")
a = id // 10000000
b = (id - (a * 10000000)) // 1000000
c = (id - (a * 10000000) - (b * 1000000)) // 100000
d = (id - (a * 10000000) - (b * 1000000) - (c * 100000)) // 10000
e = (id - (a * 10000000) - (b * 1000000) - (c * 100000) - (d * 10000)) // 1000
f = (id - (a * 10000000) - (b * 1000000) - (c * 100000) - (d * 10000) - (e * 1000)) // 100
g = (id - (a * 10000000) - (b * 1000000) - (c * 100000) - (d * 10000) - (e * 1000) - (f * 100)) // 10
h = (id - (a * 10000000) - (b * 1000000) - (c * 100000) - (d * 10000) - (e * 1000) - (f * 100) - (g * 10)) // 1
sum = (a * 8) + (b * 7) + (c * 6) + (d * 5) + (e * 4) + (f * 3) + (g * 2) + (h * 1)
if sum % 11 == 0:
    if sum % 11 >= 16:
        print("FACULTY")
    else:
        print("STUDENT")
else:
    print("INVALID")
print(" ")
any = input("Press any key to continue...")
print(" ")

            

    
