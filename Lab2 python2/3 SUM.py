'''จงเขียนฟังก์ชันเพื่อหาผลรวมของ 3 พจน์ใดๆใน Array ที่มีผลรวมเท่ากับ 0 สำหรับ Array ที่มีข้อมูลข้างในเป็นจำนวนจริง ***Array ต้องมีความยาวตั้งแต่ 3 จำนวนขึ้นไป***'''

numList = list(map(int,input("Enter Your List : ").split()))
if len(numList) < 3:
    print("Array Input Length Must More Than 2")
else:
    ans = []
    for i in range(0,len(numList)):
        for j in range(i+1,len(numList)):
            for k in range(j+1,len(numList)):
                check = True
                if numList[i] + numList[j] + numList[k] == 0:
                    temp = [numList[i], numList[j], numList[k]]
                    test1 = set(temp)
                    for a in ans:
                        test2 = set(a)
                        if test1 == test2:
                            check = False
                    if check == True:
                        ans.append(temp)
    print(ans)
