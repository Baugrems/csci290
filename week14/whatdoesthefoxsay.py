# https://open.kattis.com/problems/whatdoesthefoxsay


def foxsays(recording,sounds): # this is a simple solution once I thought of it. Function is for testing
    recording = [sound for sound in recording if sound not in sounds] # trim sounds from recording from other animals
    return " ".join(recording) # join the new trimmed list to a string
        

def main():
    cases = int(input()) # amount of cases to do

    for case in range(cases): # do this for all cases
        recording = input().split() # make a list of sounds that animals make
        sounds = [] # empty to store the sounds we find in input
        animal = input() # first line animal goes something
        while animal != "what does the fox say?": # loop until we are asked...
            sounds.append(animal.split()[-1]) # we only care about the sound, not which animal, grab last element
            animal = input() # grab next animal goes what
        result = foxsays(recording,sounds) # trim the list down
        print(result)

if __name__ == '__main__':
    main()