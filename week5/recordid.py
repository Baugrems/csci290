

command = input()
amount = int(input())
startID = input()

dataCenter = startID[-1]
startID = startID[:-1]

reserved = startID[:2]

prefix = startID[2]

recordID = int(startID[3:5], 16)
records = []
for n in range(amount):
    recordID += 1
    record = reserved + prefix + str(hex(recordID)) + dataCenter
    records.append(record)
print(records)