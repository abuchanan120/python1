# Andrew Buchanan
# Python 1 Programming Assignment 8
# December 6, 2021
# Object Oriented Programming
import random

class Bird:

    #attributes
    classification = "bird"
    colors = ["blue", "red", "grey", "black", "brown"]

    #instance method allows user to assign bird name and gives it a random color
    def __init__(self, name):
        self.name = name
        self.color = random.choice(Bird.colors)

    #reads a Bird object's attributes back to the user
    def readAttributes(self):
        print("My name is ", self.name, " and I am a ", self.color," ", self.classification, sep="")

# Main code execution
print("What would you like to name your bird?")
birdname1 = input()
print("Nice name! What about your second bird?")
birdname2 = input()
bird1 = Bird(birdname1)
bird2 = Bird(birdname2)
bird1.readAttributes()
bird2.readAttributes()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
