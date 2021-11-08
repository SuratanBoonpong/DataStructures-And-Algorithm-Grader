def sortFootballClubs(lists):
    sortedLists = []
    for i in lists:
        templist = []
        templist.append(i[0])
        templist.append({"points":(3*int(i[1])+int(i[3]))}) # 3 * wins + 0 * loss + 1 * draws = 3 * wins + draws
        templist.append({"gd":int(i[4])-int(i[5])})
        sortedLists.append(templist)

    for i in range(len(sortedLists)):
        swapped = False
        for j in range(0,len(sortedLists)-i-1):
            if (sortedLists[j][1].get("points") < sortedLists[j+1][1].get("points")) or (sortedLists[j][1].get("points") == sortedLists[j+1][1].get("points") and sortedLists[j][2].get("gd") < sortedLists[j+1][2].get("gd")):
                sortedLists[j],sortedLists[j+1] = sortedLists[j+1],sortedLists[j]
                swapped = True
        if swapped == False:
            break

    return sortedLists

lists = input("Enter Input : ").split("/")
teamList = []
for i in lists:
    tempList = i.split(",")
    teamList.append(tempList)
answerList = sortFootballClubs(teamList)
print("== results ==")
for i in answerList:
    print(i)