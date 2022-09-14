print("*** String Rotation ***")
str1,str2 = input("Enter 2 strings : ").split(" ")
copy1 = ""
copy1 += str1[len(str1)-1:]+str1[:len(str1)-1]
copy2 = ""
copy2 += str2[1:]+str2[:1]
num = 1
print(num,copy1,copy2)
while str1 != copy1 or str2 != copy2:
    temp1 = ""
    temp1 += copy1[len(copy1)-1:]+copy1[:len(copy1)-1]
    copy1 = temp1
    temp2 = ""
    temp2 += copy2[1:]+copy2[:1]
    copy2 = temp2
    num+=1
    if num <= 5:
        print(num,copy1,copy2)
if num == 6:
    print(num,str1,str2)
elif num>5:
    print(" . . . . . ")
    print(num,str1,str2)

print("Total of  "+str(num)+" rounds.")
    