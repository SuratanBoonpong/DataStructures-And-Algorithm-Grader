'''****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

ให้เขียน Recursive หาค่า Min ของ Input'''
def min(arr,num):
    if len(arr) == 0:
        return num
    if num > arr[0]:
        num = arr[0]
    arr.pop(0)
    return min(arr,num)

l = list(map(int,input("Enter Input : ").split()))
print("Min : " + str(min(l,l[0])))