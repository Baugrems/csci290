# https://open.kattis.com/problems/bookingaroom

import random # randomint needed to grab our random available room

def findRoom(amount, used, rooms): # simple function for returning either a random room or "too late"
    if amount == used: # base case of sorts. If used rooms are same as total, we are done.
        return "too late"
    room = 1 # start room at 1, maybe it's open
    while room in rooms: # while our random or starter room is occupied, select another
        room = random.randint(1,amount) # from 1, there is no room 0
    return room
    

def main():
    roomData = input() # first input line
    amount, used = [int(x) for x in roomData.split()] # make them ints
    rooms = [] # empty to store occupied rooms
    for n in range(used):
        rooms.append(int(input())) # make them ints for ease of comparison
    result = findRoom(amount, used, rooms) 
    print(result) # finally, print that result

    
if __name__ == '__main__':
    main()