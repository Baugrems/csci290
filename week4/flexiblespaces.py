def handlePartitions(partitions, width): # dont seem to need P? weird.
    partitions.append(width) # add width as a partition we should calculate
    possible = set() # use a set for unique answers
    for partition in partitions: # loop over all these things
        possible.add(partition) # make each possible size the partition spots, as those can close alone with start wall
        for compared in partitions: # do another loop over same data
            if partition is compared: # dont compare to self
                break
            possible.add(abs(compared-partition)) # add in the size of difference between 2 partitions
    return " ".join(str(x) for x in sorted(possible)) # big ugly join as strings to output nicely

if __name__ == '__main__':
    width, pSize = [int(x) for x in input().split()]
    partitions = [int(x) for x in input().split()] # input... nothing to see here
    handlePartitions(partitions, width)