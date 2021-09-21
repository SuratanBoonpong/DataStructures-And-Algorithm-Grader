'''****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

เขียน Recursive เพื่อหาว่าเลขตั้งแต่ 0 จนถึง ( 2^(input) ) - 1 นั้นมีตัวอะไรบ้าง  หากเป็นเลขติดลบให้แสดงผลเป็น Only Positive & Zero Number ! ! ! 

*** ตัวอย่างเช่น ถ้าหาก input = 2 ก็ต้องแสดงผลลัพธ์เป็น 00 , 01 , 10 , 11'''

def bin(dec,start,size):
    if start < size-1:
        bin(dec//2,start+1,size)
    print(dec%2,end='')
def numinbinary(min,size,max):
    if(min<max):
        bin(min,0,size)
        print("")
        numinbinary(min+1,size,max)
n = input("Enter Number : ")
n = int(n)
if(n<0):
    print("Only Positive & Zero Number ! ! !")
elif(n==0):
    print("0")
else:
    numinbinary(0,n,2**n)