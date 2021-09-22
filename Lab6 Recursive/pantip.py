def pantip(k, n, arr, path):
    if n == k:
        temp = path
        print(' '.join(map(str, path))) 
        return 1
    if n > k or len(arr) == 0:
        return 0
    arr1 = []+path
    arr1.append(arr[0])
    num = arr[0]
    temp1 = arr+[]
    temp2 = arr+[]
    temp1.pop(0)
    temp2.pop(0)
    return pantip(k,n+num,temp1,arr1)+pantip(k,n,temp2,path)
    
inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
pattern = pantip(int(inp[0]), 0, arr, [])
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], pattern))