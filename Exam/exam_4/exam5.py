count = 0
def mergeSort(lists):
    global count
    if len(lists) > 1:
        mid = len(lists)//2
        Llist = lists[:mid]
        Rlist = lists[mid:]
        mergeSort(Llist)
        mergeSort(Rlist)
        i = j = k = 0
        while i < len(Llist) and j < len(Rlist):
            if Llist[i] < Rlist[j]:
                lists[k] = Llist[i]
                i += 1
            else:
                lists[k] = Rlist[j]
                j +=1 
            k += 1
            count += 1
        
        while i < len(Llist):
            lists[k] = Llist[i]
            i += 1
            k += 1

        while j < len(Rlist):
            lists[k] = Rlist[j]
            j += 1
            k += 1
print(" *** Merge sort ***")
lists = list(map(int,input("Enter some numbers : ").split()))
mergeSort(lists)
print("")
print("Sorted -> ",end="")
for i in lists:
    print(str(i),end=" ")
print("")
print("Data comparison =  "+str(count))