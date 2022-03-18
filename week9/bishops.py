def bishopCounter(n):
    if n == 0 or n == 1: # base case, no need to math
        print(n)
    else:
        print((n-1) * 2) # why would we use recursion for this? I'm confused.

while True:
    try:
        n = int(input()) # grab all the input until we can't
    except EOFError:
        break
    bishopCounter(n) # print the max count