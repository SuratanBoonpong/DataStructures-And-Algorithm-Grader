'''****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

เขียน Recursive เพื่อหาว่า String ที่รับเข้ามาเป็น Palindrome หรือไม่'''

def palindrome(string,size):
    if size == 0 or size == 1:
        return 1
    else:
        if string[0] == string[-1]:
            return palindrome(string[1:size-1],size-2)
        else:
            return 0

string = input("Enter Input : ")
if(palindrome(string,len(string))):
    print("'"+string+"'"+" is palindrome")
else:
    print("'"+string+"'"+" is not palindrome")