
# INPUT
line = input()
line = line.upper() # ensure valid upper case input here (could also check for ints or symbols elsewhere.. but eh)

# SET UP
pairs = {}  # empty dict
char = 'A' # start chars at A
for x in range(26): # 26 letters in alphabet...
    pairs[char] = x # insert index for each char here
    char = chr(ord(char) + 1) # increment char to next one up


####### SPLIT #############
A = line[:int(len(line)/2)] # get first half of string
B = line[int(len(line)/2):] # get second half of string


########### ROTATE ############
rotA = 0
rotB = 0
for ch in A: # sum up rotation cost of A here
    rotA += pairs[ch]
for ch in B:
    rotB += pairs[ch] # sum up rotation cost of B here
# print(rotA, rotB) # test print to make sure values are proper
A2 = "" # new empty string for rotated A
for ch in A:
    index = (pairs[ch] + rotA) % 26 # index of each char plus rotation, then modulus of 26 to clamp it from A-Z
    A2 += (list(pairs.keys())[list(pairs.values()).index(index)])  # Prints letter at said index in my map
B2 = ""
for ch in B:
    index = (pairs[ch] + rotB) % 26 # index of each char plus rotation, then modulus of 26 to clamp it from A-Z
    B2 += (list(pairs.keys())[list(pairs.values()).index(index)])  # Prints letter at said index in my map

########### MERGE #########

result = ""
for x in range(len(A2)):
    index = (pairs[A2[x]] + pairs[B2[x]]) % 26 # clamps the merging of the two halves within A-Z
    result += (list(pairs.keys())[list(pairs.values()).index(index)])  # Prints letter at said index in my map
print(result)

