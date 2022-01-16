amt = int(input())
words = []
for x in range(amt):
    line = input()
    words.append(line)
i = 0
for word in words:
    if i % 2 == 1:
        i+=1
        continue
    i+=1
    print(word)
