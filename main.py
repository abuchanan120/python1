# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random



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
    start=1 #Allows user to start playing, keep playing, or stop playing
    done=0 #Shows when a user has played a game already
    while start==1:
        print("Which game would you like to play?")
        print("[1] - Array Art")
        print("[2] - Coin Flip")
        game=int(input())
        #Chooses which function to run based off which game was chosen
        if game==1:
            array_art()
            done=1
        elif game==2:
            coin_flip()
            done=1
        else:
            print("Please choose one of the available options.")

        #Asks if the user wants to play again after a game was played
        if done==1:
            print("Would you like to play another game? [Y/N]")
            again=input().lower()
            if again=='y':
                continue
            else:
                start=0
                break
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
