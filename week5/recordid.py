while True: # loop until we decide to exit
    command = input("Enter a command: (assign, quit)\n") 
    command = command.lower() # lower case to make it more user friendly (read: idiot proof)
    if command == "quit":
        print("Goodbye!")
        exit(0) # kill the program when user quits
    if command == "assign":
        try: 
            amount = int(input("How many IDs?\n"))
            startID = "" 
            while len(startID) != 6: # only accept IDs with proper amount of digits
                startID = input("Enter the starting ID:\n")
                if len(startID) != 6:
                    print("Improper input. Try again.")
            dataCenter = startID[-1] # last digit is the data center id. keep it as a string, we dont change it

            reserved = startID[:2] # first 2 are reserved, should be 0 but doesnt really matter for now

            prefix = startID[2] # 3rd element is the prefix

            recordID = int(startID[3:5], 16) # grab the recordID from starting ID submission, making sure to recognize it as hexadecimal
            records = []
            for n in range(amount):
                recordID += 1
                if recordID > 255: # 255 is ff in hex. This would make it more than 6 digits. Exit and print the ones that are valid.
                    print("Limit of IDs reached! Consider changing process to allow use of reserved bits.\nPrinting valid IDs if any were present.\n")
                    break
                else:
                    record = reserved + prefix + str(format(recordID, 'x')) + dataCenter  # combine all the parts for new IDs incremented properly, format hex from int counter
                    records.append(record)
            print("New IDs:")
            for record in records: # prints whatever valid IDs we made
                print(record)
        except ValueError: # catch any issues with improper integer input. Make user retry.
            print("Input is invalid.  Try again!")
    else:
        print("Not a valid command. Try assign or quit.\n") # catch-all for input being incorrect