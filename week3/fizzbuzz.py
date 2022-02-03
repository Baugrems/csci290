# INPUT
line = input()

#Split it into three ints
X, Y, N = line.split()
X = int(X)
Y = int(Y) # this is awful but I forgot the better way and wanted to finish quickly
N = int(N)
# SOLVE LOOP
for num in range(1,N + 1): # increment from 1 to N
    msg = "" # empty message
    if num % X == 0: # if divisible by X
        msg += "Fizz" # add Fizz to message, allows easy combo without more if statements
    if num % Y == 0: # if divisible by Y
        msg += "Buzz" # add Buzz to message, allows easy combo without more if statements
    if msg == "":
        print(num) # if we never set a message, make it the number
    else:
        print(msg) # if message, print it.
