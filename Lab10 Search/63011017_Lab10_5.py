def minimumWeight(lists, box):
    minWeight = 99999999

    if box == 1:
        return sum(lists)

    for i in range(len(lists)):
        if len(lists[i:]) < box - 1:
            break

        thisBox = sum(lists[:i])
        otherBox = minimumWeight(lists[i:], box - 1)
        minWeight = min(max(thisBox, otherBox), minWeight)

    return minWeight

lists, numOfBox = input("Enter Input : ").split('/')
numOfBox = int(numOfBox)
lists = list(map(int,lists.split()))
print("Minimum weigth for "+str(numOfBox)+" box(es) = "+str(minimumWeight(lists,numOfBox)))

