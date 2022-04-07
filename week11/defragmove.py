def recordIDold(startID): # throwing old version into a function per feedback from week 5
    dataCenter = startID[-1] # last digit is the data center id. keep it as a string, we dont change it
    dataCenter2 = startID[0] # first digit is new data center element as well


    prefix = startID[2] # 3rd element is the prefix

    newID = startID[1] # 2nd element is possibly part of ID now
    recordID = newID + startID[3:5] # full recordID is now 3 digits
    recordID = int(recordID, 16) # convert to hex
    records = []
    for n in range(amount):
        recordID += 1
        if recordID > 4095: # Now that we can do FFF as max, we can do 4095 IDs vs 255
            break
        else:
            recordIDdigits = f'{format(recordID, "#04x"):^3}'.upper() # pad hex with 0 if needed
            recordIDdigits = recordIDdigits[2:] # cut off the 0x of Hex
            if recordID > 255: # new case for adding extra digits
                frontI = recordIDdigits[0]
                record = dataCenter2 + frontI + prefix + recordIDdigits[1:] + dataCenter  # combine all the parts for new IDs incremented properly, format hex from int counter
            else:
                record = dataCenter2 + prefix + recordIDdigits + dataCenter  # combine all the parts for new IDs incremented properly, format hex from int counter
            records.append(record)
    return records

def defragMove(recordids, dataCenter): # new conditions to new function
    records = []
    kDict = {} # keep track of K values and their indexes
    for record in recordids:
        record = record.upper()
        # set the first and last elements to new data center
        if record[2] in kDict: # set dictionary for the K value to one higher or start at 000
            kDict[record[2]] += 1
        else:
            kDict[record[2]] = 0
        recordid = f'{format(kDict[record[2]], "#04x"):^3}'.upper() # pad hex with 0 if needed
        recordid = recordid[2:] # trim the leading 0x
        if len(recordid) == 2: # make sure its padded for 3
            recordid = "0" + recordid
        # this is silly, dont judge me
        finalRecord = dataCenter[0] + recordid[0] + record[2] + recordid[1] + recordid[2] + dataCenter[1]
        records.append(finalRecord)
    return records


# user interface portion
if __name__ == '__main__':
    while True: # loop until we decide to exit
        command = input() #assign, defrag-move, quit
        command = command.lower() # lower case to make it more user friendly (read: idiot proof)
        if command == "quit":
            exit(0) # kill the program when user quits
        if command == "assign":
            try: 
                amount = int(input())
                startID = "" 
                while len(startID) != 6: # only accept IDs with proper amount of digits
                    startID = input()
                    if len(startID) != 6:
                        print("Improper input. Try again.")
                records = recordIDold(startID) # call old function to get IDs old way
                for record in records: # prints whatever valid IDs we made
                    print(record)
            except ValueError: # catch any issues with improper integer input. Make user retry.
                print("Input is invalid.  Try again!")

        # new stuff here. UI side for defrag move
        if command == "defrag-move":
            newDataCenter = input() # pull new data center info
            amt = int(input()) # how many IDs to defrag
            recordids = [] 
            for n in range(amt): # get the new info
                recordids.append(input()) 
            records = defragMove(recordids, newDataCenter) # pull records from defrag
            for record in records:
                print(record)
        else:
            pass # if error, ignore it. Make them retry on their own.