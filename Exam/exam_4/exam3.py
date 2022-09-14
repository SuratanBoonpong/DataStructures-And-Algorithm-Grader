count = 0
def insertionSort(arr):
    global count 
    for i in range(1,len(arr)):
        temp = arr[i]
        for j in range(i,-1,-1):
            if temp<arr[j-1] and j>0:
                count += 1
                arr[j] = arr[j-1]
            else:
                if j>0:
                    count += 1
                arr[j] = temp
                break

print(" *** Insertion sort ***")
lists = list(map(int,input("Enter some numbers : ").split()))
insertionSort(lists)
print("")
print(lists)
print("Data comparison =  "+str(count))