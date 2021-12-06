# Andrew Buchanan
# Python 1 Programming Assignment 8
# December 6, 2021
# Object Oriented Programming
import random

class Bird:

    #attributes
    classification = "bird"
    colors = ["blue", "red", "grey", "black", "brown", "orange", "white", "purple",
              "blue", "red", "grey", "black", "brown", "orange", "white", "purple",
              "blue", "red", "grey", "black", "brown", "orange", "white", "purple",
              "blue", "red", "grey", "black", "brown", "orange", "white", "purple",
              "ultra-rare rainbow"]

    #instance method allows user to assign bird name and gives it a random color
    def __init__(self, name):
        self.name = name

    #reads a Bird object's attributes back to the user
    def readAttributes(self):
        print("My name is ", self.name, " and I am a ", self.color," ", self.classification, sep="")

    #sets a Bird's color attribute by allowing the user to choose or randomize from the above colors list
    def setColor(self,color):
        if (color=="random"):
            self.color = random.choice(Bird.colors)
        else:
            self.color = color

# Main code execution
print("What would you like to name your bird?")
birdname1 = input()
print("Nice name! What about your second bird?")
birdname2 = input()
bird1 = Bird(birdname1)
bird2 = Bird(birdname2)
print("What color bird is it? (Enter 'random' to randomize its color)")
birdcolor1 = input()
print("What about the second bird? (Enter 'random' to randomize its color)")
birdcolor2 = input()
bird1.setColor(birdcolor1)
bird2.setColor(birdcolor2)
bird1.readAttributes()
bird2.readAttributes()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
