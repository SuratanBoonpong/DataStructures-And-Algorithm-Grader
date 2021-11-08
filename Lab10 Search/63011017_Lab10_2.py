def bi_search(l, r, arr, x):
    if r<l:
        if l == len(arr):
            return 'No First Greater Value'
        else:
            return arr[l]
    else:
        if x > arr[int((r+l)/2)]:
            return bi_search(int((r+l)/2)+1,r,arr,x)
        elif x == arr[int((r+l)/2)]:
            if int((r+l)/2) == len(arr)-1:
                return 'No First Greater Value'
            else:
                return arr[int((r+l)/2)+1]
        else:
            return bi_search(l,int((r+l)/2)-1,arr,x)
        
inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), inp[1]
for i in k.split():
    print(bi_search(0, len(arr) - 1, sorted(arr), int(i)))