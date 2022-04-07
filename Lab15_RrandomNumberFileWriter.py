import random


def randomNumbersFile():
    randomNumbers = open('randomNumbers.txt', 'w')
    randomNumbers.close()


def amountOfNumbers():
    amtOfNumbers = int(input("Enter the amount of random numbers to generate into the file. (minimum 13): "))
    while amtOfNumbers < 13:
        print("ERROR: Amount of random numbers must be 13 or greater.\n")
        amtOfNumbers = int(input("Enter the amount of random numbers to generate into the file. (minimum 13): "))
    return amtOfNumbers


def randomGenerator(amtOfNumbers):
    for x in range(amtOfNumbers):

        totalOfNum = 0
        highestNum = 0
        lowestNum = 0
        numGenerated = 0

        generatedNum = random.randint(1, 500)
        totalOfNum += generatedNum
        averageOfnum = totalOfNum / amtOfNumbers

        if highestNum < generatedNum:
            highestNum = generatedNum
        if lowestNum > generatedNum:
            lowestNum = generatedNum

        randomNumbers = open('randomNumbers.txt', 'a')
        randomNumbers.write(f'{generatedNum}\n')
        randomNumbers.close()

        numGenerated += 1
    return totalOfNum, averageOfnum, highestNum, numGenerated, lowestNum

def printData(totalOfNum, averageOfnum, highestNum, numGenerated, lowestNum):
    infile = open('randomNumbers.txt', 'r')
    readFile = infile.read()
    print(readFile)
    print("Total: ", totalOfNum)
    print("Average: ", averageOfnum)
    print("Highest Number: ", highestNum)
    print("Numbers generated: ", numGenerated)
    print("Lowest Number: ", lowestNum)


def main():
    randomNumbersFile()
    amount = amountOfNumbers()
    total, average, highest, nums, lowest = randomGenerator(amount)
    printData(total, average, highest, nums, lowest)


main()
