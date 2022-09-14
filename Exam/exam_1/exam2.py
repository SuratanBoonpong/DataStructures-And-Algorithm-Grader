num = input("Input : ")
num = int(num)
if num <= 0:
    print("!!!Please enter number greater than zero!!!")
else:
    print("")
    for i in range(1,num):
        print(("*"*i)+(" "*(2*(num-i)))+("*"*i))
    print("*"*(num*2))
    for i in range(num-1,-1,-1):
        print(("*"*i)+(" "*(2*(num-i)))+("*"*i))