def recurse(arr,index): # this hits recursion limit and fails in Kattis...
    if index < 0: # base case
        return #end printing
    print(arr[index]) # just print instead of saving new array positions
    return recurse(arr, index - 1) # recruse...

n = int(input()) # grab amount of numbers

arr = []
for x in range(n):
    arr.append(int(input())) # save them all to array

recurse(arr, n - 1) # begin recursion