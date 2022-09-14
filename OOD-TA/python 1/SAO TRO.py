import math
def sequence(n):
    x = int(math.floor((-1 +math.sqrt(1 + 8 * n - 8)) / 2))
    b = (x * (x + 1)) / 2 + 1
    return int(n-b+1);
print("*** SAO TRO ***")
number = int(input("Input : "))
h = int(((number+1)*number)/2);
for i in range(h):
    for j in range((number*2)-1):
        btemp = sequence(i+1)
        ctemp = abs((number-1)-j)
        if((btemp%2==0 and ctemp<btemp and ctemp%2==1) or (btemp%2==1 and ctemp<btemp and ctemp%2==0)):
            print("*",end="")
        else:
            print(" ",end="")
    print()
