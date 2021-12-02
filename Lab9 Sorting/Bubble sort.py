'''

รับ input เป็น list แล้วแสดงขั้นตอนของ bubble sort ตามตัวอย่าง

***ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort เช่น .sort ให้น้องเขียนฟังก์ชัน Sort เอง และห้าม Import***'''

lists = list(map(int,input("Enter Input : ").split(" ")))
for i in range(len(lists)-1):
    swapped = False
    move = [None]
    for j in range(0,len(lists)-i-1):
        if lists[j] > lists[j+1]:
            if not lists[j] in move:
                move.pop()
                move.append(lists[j])
            lists[j], lists[j+1] = lists[j+1], lists[j]
            swapped = True
    if swapped == False or i == len(lists)-2:
        print("last step : " +str(lists)+" move"+str(move))
        break
    else:
        print(str(i+1)+" step : "+str(lists)+" move"+str(move))
    


