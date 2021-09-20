'''
อยากให้นักศึกษาช่วยหาลำดับการ Countdown จาก Input ที่รับเข้ามา 
โดยลำดับการ Countdown จะเป็นเลขเรียงลำดับ เช่น 2->1 , 3->2->1 โดยจะสิ้นสุดด้วย 1 เสมอ
โดยผลลัพธ์ให้แสดง List ของ จำนวนลำดับที่เจอ และ แต่ละลำดับเป็นอย่างไร
'''
print("*** Fun with countdown ***")
x =  list(map(int,input("Enter List : ").split()))
index = []
i = len(x)-1
while i>=0:
    if x[i] == 1:
        j = i
        temp = []
        temp.append(x[j])
        while x[j-1]-x[j] == 1:
            temp.append(x[j-1])
            j-=1 
            if j<=0:
                break
        temp.sort(reverse=True)
        index.append(temp)
        i=j
    i-=1
index.reverse()
print("[{0}, {1}]".format(len(index),index))