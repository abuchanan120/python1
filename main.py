# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random


def print_inputs():
    #Ask for name and print to output
    print("What is your name?")
    name=input()
    print("Your name is:",name)
    #Ask for a number, square it, and display it
    print("Enter a number:")
    number=int(input())
    print(number, " multiplied by ",number,"= ",number * number,sep="")
    #Ask for a word, display the number of letters
    print("Enter a word:")
    word=input()
    print("Number of letters in ",word,": ",word.__len__(),sep="")

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def array_art():
    arr=[['.', 'O', '.', 'O', '.', 'O', '.'],
        ['.', 'O', '.', 'O', '.', 'O', '.'],
        ['O', '.', 'O', '.', 'O', '.', 'O'],
        ['O', '.', 'O', '.', 'O', '.', 'O'],
        ['.', 'O', '.', 'O', '.', 'O', '.'],
        ['O', '.', 'O', '.', 'O', '.', 'O'],
        ['O', '.', 'O', '.', 'O', '.', 'O'],
        ['.', 'O', '.', 'O', '.', 'O', '.'],
        ['.', 'O', '.', 'O', '.', 'O', '.']]
    for i in range(len(arr[0])): #for every column (length of each row = number of columns)
        for k in range(len(arr)): #select a row (length of the array = number of rows)
            print(arr[k][i], end="") #print the element in row,col
        print() #carriage-return

def coin_flip():
    #Prompt for user choice
    print("Please choose either 0 or 1:")
    choice=int(input())

    #Choose 0 or 1 randomly
    answer=random.randint(0, 1)

    #Figure out if choice is correct
    if choice==answer:
        print("You win!")
    else:
        print("The Computer wins!")

# Main code execution
if __name__ == '__main__':

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
