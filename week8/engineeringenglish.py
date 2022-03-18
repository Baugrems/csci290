import sys

lines = sys.stdin.read().split("\n")[:-1]

seen = []

for line in lines:
    words = line.split()
    output = []
    for word in words:
        word = word.lower()
        if word in seen:
            output.append(".")
        else:
            output.append(word)
            seen.append(word)
    print(" ".join(output))