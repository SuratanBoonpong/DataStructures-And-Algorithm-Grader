def bi_search(l, r, arr, x):
    if r<l:
        return False
    else:
        if x > arr[int((r+l)/2)]:
            return bi_search(int((r+l)/2)+1,r,arr,x)
        elif x == arr[int((r+l)/2)]:
            return True
        else:
            return bi_search(l,int((r+l)/2)-1,arr,x)
        
inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))