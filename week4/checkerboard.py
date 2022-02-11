def handleBoard(rows):
    #ROWS
    for row in rows: # do all rows first, then columns will be later
        colors = {"W": 0, "B": 0} # reset map for row to be 0 for white and black
        for i in range(len(row)): # loop over the row of characters
            if i > 0 and i < len(row) - 1:
                if row[i] == row[i-1] and row[i] == row[i+1]: # this ugly mess checks if we have 3 consecutive matches, thus being invalid.
                    return 0
            colors[row[i]] += 1 # whatever the color is at this part, increment its count
        if colors["W"] != colors["B"]: # same W and B in a row? If not, fail.
            return 0
    #COLUMNS
    for i in range(len(rows)): # looping over columns here
        colors = {"W": 0, "B": 0} # reset map for column to be 0 for white and black
        for j in range(len(rows)):
            if j > 0 and j < len(rows) - 1:
                if rows[j][i] == rows[j-1][i] and rows[j][i] == rows[j+1][i]: # this ugly mess checks if we have 3 consecutive matches, thus being invalid.
                    # print(rows)
                    return 0
            colors[rows[j][i]] += 1 # incrementing our count for W or B.
        # print(colors, rows[j])
        if colors["W"] != colors["B"]: # Same W and B in a column? If not, fail.
            # print("Column fail")
            return 0
    return 1 # if we didn't return yet, we did it. Send out the 1



if __name__ == '__main__':
    amt = int(input())

    rows = []

    for x in range(amt): # just grabbing input nothing to see here
        row = input()
        rows.append(row)

    handleBoard(rows)


