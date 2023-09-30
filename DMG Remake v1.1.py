import math
from random import randint

version = "1.1"

# Values

money = 1000
multiplier = 1
gameActive = False
currencySymbol = str

trophies = [
    "Bronze-Trophy",
    False, # Bronze Trophy
    "Silver-Trophy",
    False, # Silver Trophy
    "Gold-Trophy",
    False, # Gold Trophy
    "Diamond-Trophy",
    False, # Diamond Trophy
    "Platinum-Trophy",
    False, # Platinum Trophy
    "Hacker-Trophy",
    False # Hacker Trophy
]

def startMsg():
    print(f"""
    This is a remake of Digital Miner Game by AF2603 (123 Game#8926)
    Original by Turtle (TurtleBoy#6915)

    Commands:

    money      | Shows how much money you have.
    multiplier | Shows your current multiplier.
    shop       | Opens the shop.
    trophies   | Shows what tropys you have unlocked and what is still locked!
    cmds       | Shows this menu.
    end        | Ends the current game.

    [ENTER]    | Mines.

    Made with Python
    Version ({version})

    """)

startMsg()

def shop():
    global money
    global multiplier
    global currencySymbol
    multiplier = multiplier
    money = money
    currencySymbol = currencySymbol

    moneyFormatted = "{:,.2f}".format(money)

    print(f"""
    Upgrades:

    Multiplier + 5 (m5)       | {currencySymbol}4,000
    Multiplier + 25 (m25)     | {currencySymbol}25,000
    Multiplier + 100 (m100)   | {currencySymbol}95,000
    Multiplier + 500 (m500)   | {currencySymbol}510,000
    Multiplier + 5000 (m5000) | {currencySymbol}5,000,000

    Multiplier x 5 (5m)       | {currencySymbol}500,000,000
    Multiplier x 15 (15m)     | {currencySymbol}1,500,000,000

    Money: {currencySymbol}{moneyFormatted}

    Press [enter] to exit.
    """)
    userSelection = input("Shop: ").lower()

    if userSelection == "" or userSelection == "exit":
        print("Leaving shop...")
    elif userSelection == "m5":
        if money >= 4000:
            money = money - 4000
            multiplier = multiplier + 5

            print("Purchased!")
        else:
            print("Insufficent funds!")
    elif userSelection == "m25":
        if money >= 25000:
            money = money - 25000
            multiplier = multiplier + 25

            print("Purchased!")
        else:
            print("Insufficent funds!")
    elif userSelection == "m100":
        if money >= 95000:
            money = money - 95000
            multiplier = multiplier + 100

            print("Purchased!")
        else:
            print("Insufficent funds!")
    elif userSelection == "m500":
        if money >= 510000:
            money = money - 510000
            multiplier = multiplier + 500

            print("Purchased!")
        else:
            print("Insufficent funds!")
    elif userSelection == "m5000":
        if money >= 5000000:
            money = money - 5000000
            multiplier = multiplier + 5000

            print("Purchased!")
        else:
            print("Insufficent funds!")
    elif userSelection == "5m":
        if money >= 500000000:
            money = money - 500000000
            multiplier = multiplier * 5

            print("Purchased!")
        else:
            print("Insufficent funds!")
    elif userSelection == "15m":
        if money >= 1500000000:
            money = money - 1500000000
            multiplier = multiplier * 15

            print("Purchased!")
        else:
            print("Insufficent funds!")
    else:
        print("Invalid input!")
        shop()

while gameActive == False:
    optionInput = input("Would you like to start? (y/n) > ").lower()

    if optionInput == "y" or optionInput == "yes":

        option2Input = input("\nPlease select your currency. (£, $, €) > ")

        if option2Input == "£":
            currencySymbol = "£"
            gameActive = True

            print("\nNew game started!\n")
        elif option2Input == "$":
            currencySymbol = "$"
            gameActive = True
            
            print("\nNew game started!\n")
        elif option2Input == "€":
            currencySymbol = "€"
            gameActive = True

            print("\nNew game started!\n")
        else:
            print("Invalid input!")
    elif optionInput == "n" or optionInput == "no":
        print("Closing...")
        break
    else:
        print("Invalid input.")

def checkTrophies():
    global money
    money = money
    global trophies
    trophies = trophies

    if money >= 1000000 and trophies[1] != True:
        trophies[1] = True

        print("\nUnlocked Bronze trophy!\n")
    elif money >= 100000000 and trophies[3] != True:
        trophies[3] = True

        print("\nUnlocked Silver trophy!\n")
    elif money >= 50000000000 and trophies[5] != True:
        trophies[5] = True

        print("\nUnlocked Gold trophy!\n")
    elif money >= 100000000000000 and trophies[7] != True:
        trophies[7] = True

        print("\nUnlocked Diamond trophy!\n")
    elif money >= 500000000000000 and trophies[9] != True:
        trophies[9] = True

        print("\nUnlocked Platinum trophy!\n")
    elif money >= math.inf and trophies[11] != True:
        trophies[11] = True

        print("\nUnlocked Hacker trophy!\n")

def displayTrophies():
    global trophies
    trophies = trophies
    global currencySymbol
    currencySymbol = currencySymbol

    unlocked = "".split()
    locked = "".split()

    for i in range(0, 11):
        if (i % 2) != 0:
            if trophies[i] == True:
                unlocked.insert(i, trophies[i - 1])
            elif trophies[i] == False:
                locked.insert(i, trophies[i - 1])

    resultUnlocked = " ".join(unlocked)
    resultLocked = " ".join(locked)
    
    # Formating the string for unlocked trohpies

    resultUnlockedFormatted = resultUnlocked
    resultUnlockedFormatted = resultUnlockedFormatted.replace(" ", "\n")
    resultUnlockedFormatted = resultUnlockedFormatted.replace("-", " ")

    # Formating the string for locked trohpies

    resultLockedFormatted = resultLocked
    resultLockedFormatted = resultLockedFormatted.replace(" ", "\n")
    resultLockedFormatted = resultLockedFormatted.replace("-", " ")

    if resultUnlockedFormatted == "":
        print(f"""
    Trophies:

    Bronze Trophy   | {currencySymbol}1,000,000
    Silver Trophy   | {currencySymbol}100,000,000
    Gold Trophy     | {currencySymbol}50,000,000,000
    Diamond Trophy  | {currencySymbol}100,000,000,000,000
    Platinum Trophy | {currencySymbol}500,000,000,000,000
    Hacker Trophy   | ???
        """)
        print("Locked:\n")
        print(f"{resultLockedFormatted}\n")
    elif resultLockedFormatted == "":
        print(f"""
    Trophies:

    Bronze Trophy   | {currencySymbol}1,000,000
    Silver Trophy   | {currencySymbol}100,000,000
    Gold Trophy     | {currencySymbol}50,000,000,000
    Diamond Trophy  | {currencySymbol}100,000,000,000,000
    Platinum Trophy | {currencySymbol}500,000,000,000,000
    Hacker Trophy   | ???
        """)
        print("Unlocked all:\n")
        print(f"{resultUnlockedFormatted}\n")
    else:
        print(f"""
    Trophies:

    Bronze Trophy   | {currencySymbol}1,000,000
    Silver Trophy   | {currencySymbol}100,000,000
    Gold Trophy     | {currencySymbol}50,000,000,000
    Diamond Trophy  | {currencySymbol}100,000,000,000,000
    Platinum Trophy | {currencySymbol}500,000,000,000,000
    Hacker Trophy   | ???
        """)
        print("Unlocked:\n")
        print(f"{resultUnlockedFormatted}\n")
        print("Locked:\n")
        print(f"{resultLockedFormatted}\n")

def mine():
    # Global variables

    global money
    global multiplier
    multiplier = multiplier

    money = money + 1 * multiplier

    print("Mined!")

    # Multiplier random upgraded

    if randint(1, 100) == 50:
        multiplier = multiplier + 0.5

        print(f"\nMultiplier increasted to {multiplier}x\n")
        
    # Diamond random pickup
        
    if randint(1, 200) == 100:
        randMoney = randint(500, 1000)
        money = money + randMoney

        print(f"\nYou found a digital diamond worth {currencySymbol}{randMoney}!\n")

    # BitCoin random pickup

    if randint(1, 500) == 250:
        bitCoinValue = randint(25000, 30000)
        money = money + bitCoinValue

        print(f"\nYou found 1 Bit Coin worth {currencySymbol}{bitCoinValue}!\n")

    # Hard drive random pickup

    if randint(1, 50) == 25:
        hardDriveValue = randint(300, 700)
        money = money + hardDriveValue

        print(f"\nYou found a Hard Drive worth {currencySymbol}{hardDriveValue}!\n")

    checkTrophies()

while gameActive == True:
    userInput = input("Press [enter] to mine: ").lower()
    
    if userInput == "":
        mine()
    elif userInput == "shop":
        shop()
    elif userInput == "money":
        print(currencySymbol,"{:,.2f}".format(money))
    elif userInput == "multiplier":
        print(f"{multiplier}x")
    elif userInput == "trophies":
        displayTrophies()
    elif userInput == "cmds" or userInput == "commands":
        moneyFormated = "{:,.2f}".format(money)

        print(f"""
    Commands:

    money      | Shows how much money you have.
    multiplier | Shows your current multiplier.
    shop       | Opens the shop.
    trophies   | Shows what tropys you have unlocked and what is still locked!
    cmds       | Shows this menu.
    end        | Ends the current game.

    Money: {currencySymbol}{moneyFormated}
    Multiplier: {multiplier}x
    Current slection: {currencySymbol}

    [ENTER] | Mines.
        """)
    elif userInput == "end" or userInput == "exit":
        confirm = input("Are you sure you want to quit? (y/n) > ").lower()

        if confirm == "y" or confirm == "yes":
            print("Quiting...")
            break
    else:
        print("\nInvalid input clasified as [enter]!\n")
        mine()