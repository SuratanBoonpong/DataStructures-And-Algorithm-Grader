def harmonic_sum(n):
    if n == 1:
        print("1",end='')
        if n == num:
            print(" = ",end='')
        return 1
    ans = harmonic_sum(n-1)+1/n
    print(" +","1/"+str(n),end='')
    if n == num:
        print(" = ",end='')
    return ans
print(" *** Harmonic sum ***")
num = int(input("Enter number of terms : ")) 
print("%.8f" %(harmonic_sum(num)))