def fac(n):
    if n < 2:
        return 1
    return n * fac(n-1)

num = input("Enter Number : ")
num = int(num)
print(str(num)+"! = "+str(fac(num)))
