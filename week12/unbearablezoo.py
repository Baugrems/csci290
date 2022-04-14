
def findAnimalCounts(animalList):
    global animals
    for animal in animalList:
        if animal in animals:
            animals[animal] += 1
        else:
            animals[animal] = 1
    keys = list(animals.keys())
    keys.sort()
    for key in keys:
        print(key, "|", animals[key])
animals = {}
if __name__ == '__main__':

    amt = 999
    listNum = 0
    while amt != 0:
        listNum += 1
        amt = int(input())
        animals = {}
        animalList = []
        for n in range(amt):
            animal = input().split()
            animal = animal[-1].lower()
            animalList.append(animal)
        if amt:
            print("List " + str(listNum) + ":")
        findAnimalCounts(animalList)