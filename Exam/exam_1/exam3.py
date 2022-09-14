print(" *** Recite the multiplication table ***")
l = list(map(int,input("Enter pattern for child 1 to 3 (-1 for sep) : ").split(" ")))
print("")
print("Pattern for child 1 : ",end="")
l1 = []
l2 = []
l3 = []
day = 0
index = 0
while index < len(l):
    if l[index] != -1:
        print(l[index],end=" ")
        l1.append(l[index])
        index += 1
    else:
        index += 1
        break
print("")
print("Pattern for child 2 : ",end="")
while index < len(l):
    if l[index] != -1:
        print(l[index],end=" ")
        l2.append(l[index])
        index += 1
    else:
        index += 1
        break
print("")
print("Pattern for child 3 : ",end="")
while index < len(l):
    if l[index] != -1:
        print(l[index],end=" ")
        l3.append(l[index])
        index += 1
    else:
        index += 1
        break

while l1[day%len(l1)] != l2[day%len(l2)] or l2[day%len(l2)] != l3[day%len(l3)] or l1[day%len(l1)] != l3[day%len(l3)]:
    if len(l1) == len(l2) and len(l2) == len(l3) and day > len(l1):
        day = 0
        break;
    day += 1
print("")
if day == 0:
    print("This year they never recite same multiplication table !!!")
else:
    print("They recite same multiplication table in "+str(day+1)+" days")