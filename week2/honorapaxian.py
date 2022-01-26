line = input()

y,p = line.split()
vowels = ['a','i', 'o', 'u']
end = y[-2:]
last = y[-1]
if end == "ex":
    print(y+p)
elif last == "e":
    print(y + "x" + p)
elif last in vowels:
    y = y[:-1]
    print(y + "ex" + p)
else:
    print(y + "ex" + p)