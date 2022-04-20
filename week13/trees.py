import math

class Pipe: # use a class to hold pipe data
    def __init__(self, parent, child, value, isSuper):
        self.parent = parent
        self.child = child
        self.value = value
        self.isSuper = isSuper

amt = int(input()) # amount of nodes

tree = {} # tree map to hold pipes under each parent node
revTree = {} # reverse map so we can work backwards easily

for n in range(amt-1): # get input and make all the pipes
    parent, child, value, sqrPipe = [int(x) for x in input().split()]
    tmp = Pipe(parent,child,value,sqrPipe)
    if parent not in tree:
        tree[parent] = []
    tree[parent].append(tmp)
    revTree[child] = parent

foodNeeds = [int(x) for x in input().split()] # last input is the needs list
most = 0 # hold the max so we make sure no ants starve
for x in range(0,amt):
    if foodNeeds[x] == -1: # if not leaf, dont process it as one
        continue
    need = foodNeeds[x] # initial needed amount
    leaf = x + 1 # index for nodes starts at 1, so... adjust
    while leaf != 1: # 1 is root, so as long we have not reached that... keep at it
        parent = revTree[leaf] # get parent node
        parent = tree[parent] # get pipes from parent node
        for pipe in parent: 
            if pipe.child == leaf: # find pipe that relates to current leaf/node
                parent = pipe
            
        if parent.isSuper: # if super pipe, square root before traversing.
            need = math.sqrt(need)
        need *= 100 # scale up for easier manipulation
        need /= parent.value # divide by the percentage
        leaf = revTree[leaf] # move on to next node above
    most = max(most,need) # choose max of found values so we feed all ants
print(most) 
