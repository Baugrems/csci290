
def findAnimalCounts(animalList):
    global animals
    for animal in animalList:
        if animal in animals: # checking if key exists in animals map
            animals[animal] += 1 # increment count by 1 if so
        else:
            animals[animal] = 1 # else start it at 1
    keys = list(animals.keys())
    keys.sort() # sort for alphabetical order so we list it correctly
    for key in keys: # print out in order the key and the value
        print(key, "|", animals[key])

animals = {}
if __name__ == '__main__':

    amt = 999
    listNum = 0
    while amt != 0: # keep accepting input until we dont have any animals wanted
        listNum += 1 # keep track of how many lists we've done
        amt = int(input())
        animals = {}
        animalList = []
        for n in range(amt):
            animal = input().split() # split by word
            animal = animal[-1].lower() # we only care about last word, the animal type
            animalList.append(animal) # add to our list, move on
        if amt:
            print("List " + str(listNum) + ":") # we need to for some reason output a list indictator here. So we do
        findAnimalCounts(animalList) 