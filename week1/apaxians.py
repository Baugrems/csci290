line = input()
i = 1
last = line[0]
result = line[0]
while i < len(line):
    if line[i] == last:
        i += 1
        continue
    last = line[i]
    
    result += line[i]
    i += 1
print(result)