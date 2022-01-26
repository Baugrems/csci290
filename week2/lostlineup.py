amt = int(input())

line = input()

line = line.split(' ')
if amt == 1:
    print("1")
elif amt < 3:
    print("1 2")
else:
    result = []
    for x in range(2, amt + 1):
        result.append(x)
    for x in range(len(line) - 1):
        for y in range(x + 1, len(line)):
            if int(line[x]) > int(line[y]):
                n = line[y]
                line[y] = line[x]
                line[x] = n
                n = result[y]
                result[y] = result[x]
                result[x] = n
    msg = "1"
    for x in result:
        msg += " " + str(x)
    print(msg)