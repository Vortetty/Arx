import sys
import consoleManager
import time as t
from classes import Hero


def beginGame():
    askName()
    askClass()
    mainChar = Hero(100, 10, classSelect)
    dialogue1()


# ------------------------------------------
# Break to indicate all the functions below:
# ------------------------------------------


def printSlow(text, typespeed=0.03, sleeptime=0, nextline=True):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        t.sleep(typespeed)
    t.sleep(sleeptime)
    if nextline == True:
        print(" ")


def askName():
    printSlow("Hello Adventurer, what is your name?")
    name = input("> ")
    while len(name) > 18 or len(name) < 3:
        if len(name) > 18:
            printSlow(
                "Ive never met an Adventurer with such a long name, what else do you go by?")
        elif len(name) < 3:
            printSlow(
                "Ive never met an Adventurer with such a short name, what else do you go by?")
        name = input("> ")
    printSlow("Welcome, %s" % name.capitalize() + " to the city of Arx!")


def askClass():
    global classSelect
    printSlow(
        "What class would you like to play, [Commoner], [Warrior], [Mage], [Thief], or [Paladin]?")
    classSelect = input("> ")
    while classSelect.lower() not in ["commoner", "warrior", "mage", "thief", "paladin"]:
        printSlow(
            "Come again, which class? [Commoner], [Warrior], [Mage], [Thief], or [Paladin].")
        classSelect = input("> ")


def dialogue1():
    printSlow(f"Agility: {mainChar.agility}")
    printSlow(f"Charisma: {mainChar.charisma}")
    printSlow(f"Intelligence: {mainChar.intelligence}")
    printSlow(f"Mana Pool Max: {mainChar.manaPoolmax}")
    printSlow(f"Stamina Pool Max: {mainChar.staminaPoolmax}")
    printSlow(f"Strength: {mainChar.strength}")
    printSlow(f"_Health: {mainChar._health}")
    printSlow(f"_Armor: {mainChar._armor}")
    printSlow(f"Health: {mainChar.health}")
    printSlow(f"Armor: {mainChar.armor}")
