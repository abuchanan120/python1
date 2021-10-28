# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

#Concatenates all arguments into a single string, separated by '-', and prints it
def joinArgs(argmt):
    print("-".join(argmt))

#Capitalizes arguments and prints them
def capitalArgs(argmt):
    for arg in argmt:
        print(arg.capitalize(), end=" ")

# Main code execution
if __name__ == '__main__':
    joinArgs(sys.argv)
    capitalArgs(sys.argv)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
