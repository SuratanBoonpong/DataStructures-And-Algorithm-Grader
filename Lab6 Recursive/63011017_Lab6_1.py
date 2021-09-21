'''****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

หาลำดับ Fibonacci ของ input ที่รับเข้ามาโดยใช้ Recursive'''

def Fibo(num):
    if num == 1:
        return 1
    elif num == 2:
        return 1
    else:
        return Fibo(num-1) + Fibo(num-2)

num = input("Enter Number : ")
print("fibo({0}) = {1}".format(num,str(Fibo(int(num)))))
