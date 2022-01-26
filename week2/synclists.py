
amt = 999
while amt != 0:
    amt = int(input())
    pairs = {"a": 0}
    list1 = []
    list2 = []
    for x in range(amt):
        list1.append(int(input()))
    for x in range(amt):
        list2.append(int(input()))
    slist1 = []
    for c in list1:
        slist1.append(c)
    slist2 = []
    for c in list2:
        slist2.append(c)
    slist1.sort()
    slist2.sort()

    for x in range(amt):
        pairs[slist1[x]] = slist2[x]
    for x in list1:
        print(pairs[x])