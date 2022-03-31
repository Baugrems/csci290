amt = int(input())

weights = []
for x in range(amt):
    weights.append(int(input()))

results = []

def calcWeights(index, wTotal):
    global weights
    global results
    if index == len(weights) - 1:
        return wTotal
    


print(calcWeights(0, 0))