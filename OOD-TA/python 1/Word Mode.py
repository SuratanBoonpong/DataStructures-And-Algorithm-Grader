input = list(input("Vote result: ").split())
max = 0
answer = []
for i in input:
    if input.count(i) == max and i not in answer:
        answer.append(i)
    elif input.count(i) > max:
        answer = [i]
        max = input.count(i)
print("top vote: ",end="")
print(*answer)
