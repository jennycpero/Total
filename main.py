import time
import random

# creates list of 10 numbers to be your set
setList = [random.randrange(1, 11, 1) for i in range(10)]
usedNum = []  # list of nums used during guess

firstTotal = -1


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score


def cancel(remove, setCopy):
    if remove in setCopy:
        print("All instances of " + str(remove) + " will be eliminated from your set!")
        setCopy[:] = (val for val in setCopy if val != remove)
    else:
        print(str(remove) + " is not in your set, so you can choose to remove all instances of another number instead.")
        remove = int(input("Type the number that you wish to remove: "))
        cancel(remove, setCopy)
    p.score += 50


p = Player("Player", 0)

# actual game
while firstTotal != 0:
    print("Here is your set of " + str(len(setList)) + " number(s): ")
    firstTotal = sum(setList)
    print(setList)
    print("The sum of this set totals to: " + str(firstTotal))
    time.sleep(2)
    addNum = random.randrange(1, 11)
    secondTotal = firstTotal + addNum
    print("\n" + str(addNum) + " added to " + str(firstTotal) + " totals to: " + str(secondTotal))
    subNum = random.randrange(1, 11)
    thirdTotal = secondTotal - subNum
    print(str(subNum) + " subtracted from " + str(secondTotal) + " totals to: " + str(thirdTotal))

    time.sleep(2)

    if firstTotal == thirdTotal and addNum == subNum:
        print("\nYou got a cancel; your first and third totals are already equal!")
        cancel(addNum, setList)
        continue
    else:
        numMoves = random.randrange(1, 11)
        print("\nUsing only " + str(numMoves) + " number(s) in your set, calculate back from your third total (" + str(
            thirdTotal) + ") to your first total (" + str(firstTotal) + ").")
        print("To win the game, reduce your set down to 0 numbers (a total of 0).")

        while numMoves > 0 and sorted(setList) != sorted(usedNum) and firstTotal != thirdTotal:
            option = input("\nWould you like to add, subtract, or give up? (A/S/G): ")
            # if they choose to give up
            if option.upper() == "G":
                print("\nOuch! Two numbers have been added to your set!")
                time.sleep(2)
                for i in range(2):
                    setList.append(random.randrange(1, 11, 1))
                break
            # if they want to add or subtract a number to/from the third total
            elif option.upper() == "A" or option.upper() == "S":
                while True:
                    try:
                        numUsed = int(input("What number?: "))
                        if numUsed in setList:
                            if option.upper() == "A":
                                thirdTotal += numUsed
                            elif option.upper() == "S":
                                thirdTotal -= numUsed
                            usedNum.append(numUsed)
                            numMoves -= 1
                            break
                        else:
                            print("You can only use numbers in your set. Try again.")
                    except ValueError:
                        print("\nNot a number. Try again.")
            else:
                print("Invalid input. Try again.")
                continue
            print("\nYour total is now: " + str(thirdTotal))
            print("Number of moves left: " + str(numMoves))
        if firstTotal == thirdTotal:
            print("You made it back to your first total! The first instances of the numbers used will be eliminated "
                  "from "
                  "your set!")
            time.sleep(3)
            for num in usedNum:
                if num in setList:
                    setList.remove(num)
            usedNum.clear()
            p.score += (10 - numMoves)
            p.score += 100
            firstTotal = sum(setList)
        elif (numMoves == 0 or sorted(setList) == sorted(usedNum)) and firstTotal != thirdTotal:
            print("Out of moves or numbers! Two more numbers have been added to your set!")
            for i in range(2):
                setList.append(random.randrange(1, 11, 1))
                usedNum.clear()
print("\nCongratulations! You've won Total!")
print("Your score: " + str(p.score))

