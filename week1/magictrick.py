line = input()
seen = set()
answer = 1
for c in line:
    if c in seen:
        answer = 0
    seen.add(c)
        
print(answer)