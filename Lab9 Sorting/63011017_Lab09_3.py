def isMetadrome(lists):
    for i in range(1,len(lists)):
        if lists[i-1] > lists[i] or lists[i-1] == lists[i]:
            return False
    return True

def isPlaindrome(lists):
    checkRepeater = False
    checkAscending = True
    for i in range(1,len(lists)):
        if lists[i-1] > lists[i]:
            checkAscending = False
        if lists[i-1] == lists[i]:
            checkRepeater = True
    return checkRepeater and checkAscending and not isRepdrome(lists)

def isKatadrome(lists):
    for i in range(1,len(lists)):
        if lists[i-1] < lists[i] or lists[i-1] == lists[i]:
            return False
    return True

def isNialpdrome(lists):
    checkRepeater = False
    checkDescending = True
    for i in range(1,len(lists)):
        if lists[i-1] < lists[i]:
            checkDescending = False
        if lists[i-1] == lists[i]:
            checkRepeater = True
    return checkRepeater and checkDescending and not isRepdrome(lists)

def isRepdrome(lists):
    for i in range(1,len(lists)-1):
        if lists[i-1] != lists[i]:
            return False
    return True

def isNondrome(lists):
    if not isMetadrome(lists)\
        and not isPlaindrome(lists)\
            and not isKatadrome(lists)\
                and not isNialpdrome(lists)\
                    and not isRepdrome(lists):
        return True
    else:
        return False

number = input("Enter Input : ")
ListOfNumber = []
for i in number:
    ListOfNumber.append(int(i))
if isMetadrome(ListOfNumber):
    print("Metadrome")
if isPlaindrome(ListOfNumber):
    print("Plaindrome")
if isKatadrome(ListOfNumber):
    print("Katadrome")
if isNialpdrome(ListOfNumber):
    print("Nialpdrome")
if isRepdrome(ListOfNumber):
    print("Repdrome")
if isNondrome(ListOfNumber):
    print("Nondrome")