'''
เขียนภาษา Python เพื่อวาดรูปหัวใจ ซึ่งจะรับ input เป็นขนาดของรูปหัวใจ โดย input จะมีค่าตั้งแต่ 2 ขึ้นไป
'''
print("*** Fun with Drawing ***")
x = int(input("Enter input : "))
for i in range(x-1,-((x*2)-1),-1):
    for j in range((x*2)-2,-((x*2)-1),-1):
        if (((i == abs(j) or abs(j)==x+(x-i)-2)) and (i>=0)) or ((i<0) and (abs(i)+abs(j)==(x*2)-2)):
            print("*",end="")
        elif (((i>abs(j)) or ((abs(j)-(x-1))+i>x-1)) and (i>=0)) or ((i<0) and (abs(i)+abs(j)>((x*2)-2))):
            print(".",end="")
        else:
            print("+",end="")
    print("")