
A,B = map(int,input("Input 2 Numbers: ").split())
if A>B:
    A,B = B,A
print("Summation Of Number Between {0} to {1} is {2}".format(A,B,int(((B*(B+1))/2)-(((A-1)*((A-1)+1))/2))))

