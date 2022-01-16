line = input()

words = []

length = int(len(line) / 3)

words.append(line[0:length])
words.append(line[length:length*2])
words.append(line[length*2:])

if words[0] == words[1]:
    print(words[0])
elif words[1] == words[2]:
    print(words[1])
else:
    print(words[2])