number = int(input("input your number: "))
answer = []
factor = 2
while number!=1:
    while number%factor == 0:
        number/=factor
        answer.append(factor)
    factor += 1
print(*answer,sep=" x ")