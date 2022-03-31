
increasing = False
decreasing = False
neither = False

def isAlphabetical(index, names):
    global increasing
    global decreasing
    global neither
    if index == len(names) - 1:
        return
    if names[index + 1] > names[index]:
        increasing = True
        if decreasing:
            neither = True
    elif names[index + 1] < names[index]:
        decreasing = True
        if increasing:
            neither = True
    return isAlphabetical(index + 1, names)
    
amt = int(input())

names = []
for x in range(amt):
    names.append(input())

isAlphabetical(0, names)
if neither:
    print("NEITHER")
elif increasing:
    print("INCREASING")
else:
    print("DECREASING")