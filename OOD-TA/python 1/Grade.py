n = int(input("input your score: "))
if n < 0 or n > 100:
    print("Invalid Input")
elif n < 40:
    print("F")
elif n < 45:
    print("D")
elif n < 50:
    print("D+")
elif n < 55:
    print("C")
elif n < 60:
    print("C+")
elif n < 65:
    print("B")
elif n < 70:
    print("B+")
elif n < 75:
    print("A")
elif n < 80:
    print("A+")
else:
    print("S")