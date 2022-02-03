# SET UP
samples = []
times = []

# INPUT
amt = int(input())
for x in range(amt): # grab each line of input here
    line = input()
    ti, vi = line.split() # split lines into two values
    ti = int(ti)
    vi = float(vi)
    times.append(ti) # save input to two arrays with matching indexes for use later
    samples.append(vi)

#SOLVE LOOP
area = 0.0
for x in range(amt - 1): # every pair needs calculated, so cut off last line
    area += ((samples[x] + samples[x+1]) / 2) * (times[x+1] - times[x]) # forumla provided, plugged in here
area /= 1000 # divide by 1000 for proper units
print(area)