line = input()

length = len(line)
whites = 0
lowers = 0
uppers = 0
symbols = 0

for x in range(length):
    c = line[x]
    if c == '_':
        whites += 1
        continue
    c = ord(c)
    if c < 97 and c > 90:
        symbols += 1
    elif c < 65 or c > 122:
        symbols += 1
    elif c < 91:
        uppers += 1
    else:
        lowers += 1

print(whites/length)
print(lowers/length)
print(uppers/length)
print(symbols/length)