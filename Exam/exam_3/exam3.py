def palindrome(string):
    if len(string) == 1 or len(string) == 0:
        return " is palindrome"
    else:
        if string[0].upper() == string[-1].upper():
            return palindrome(string[1:-1])
        else:
            return " is not palindrome"

string = input("Enter Input : ")
newstring = ''
for i in string:
    if i.isalnum():
        newstring += i
print("'"+string+"'"+palindrome(newstring))
