# I never really got back to doing this assignment. I was sick with COVID this week and just did bare minimum solving no thought on complexity. Sorry.

amt = int(input())
rolls = input()
original_rolls = [int(x) for x in rolls]
rolls = list(original_rolls)

while len(rolls) > 0:
    set_rolls = set(rolls)
    max_roll = max(set_rolls)
    if rolls.count(max_roll) > 1:
        rolls[:] = [x for x in rolls if x != max_roll]
    else:
        print(original_rolls.index(max_roll))
        break
if len(rolls) == 0:
    print("none")