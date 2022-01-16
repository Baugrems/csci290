line = input()

line = line.split('-')

result = ""

for x in range(len(line)):
    result += line[x][0]

print(result)