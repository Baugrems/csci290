line = input()
g, s, c = line.split()
g = int(g)
s = int(s)
c = int(c)
power = 0
power += (g * 3)
power += (s * 2)
power += c
if power >= 8:
    print("Province or Gold")
elif power >= 6:
    print("Duchy or Gold")
elif power == 5:
    print("Duchy or Silver")
elif power >= 3:
    print("Estate or Silver")
elif power == 2:
    print("Estate or Copper")
else:
    print("Copper")