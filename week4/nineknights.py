from collections import Counter

#This isn't very good looking, and there might be better (like using distance) but this is what I actually did for Kattis on a time crunch
def getTargets(board, y, x): # if statements check all of the 8 possible knight targets when given an x, y point
    if x > 1 and y > 0 and board[y-1][x-2] == 'k':
        return True
    if x > 0 and y > 1 and board[y-2][x-1] == 'k':
        return True
    if x > 0 and y < 3 and board[y+2][x-1] == 'k':
        return True
    if x > 1 and y > 4 and board[y+1][x-2] == 'k':
        return True
    if x < 3 and y > 0 and board[y-1][x+2] == 'k':
        return True
    if x < 4 and y > 1 and board[y-2][x+1] == 'k':
        return True
    if x < 3 and y < 3 and board[y+1][x+2] == 'k':
        return True
    if x < 4 and y > 4 and board[y+2][x+1] == 'k':
        return True
    return False

# after getting input, throw it into a loop checking every knight's ability to capture another knight.
def handleKnights(board):
    count = 0
    for row in board:
        count += Counter(row)['k'] # increments knight count based on how many per row
    if count != 9: # don't do all the hard work if we don't even have 9 knights
        return "invalid"
    for y in range(5):
        for x in range(5):
            if board[y][x] == "k":
                if getTargets(board, y, x): # returns true if it finds a capturable knight, false if not
                    # print("Knight at", x, y)
                    return "invalid"
    return "valid"

if __name__ == '__main__':
    board = []
    for i in range(5): # get input of 5 rows, as we know its always 5
        row = input()
        board.append(row)
    
    handleKnights(board)