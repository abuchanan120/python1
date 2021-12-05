# Andrew Buchanan
# Python 1 Programming Assignment 2
# Completed on time, but was submitted with another branch since it wasn't clearly specified to create a new one.

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

# Main code execution
if __name__ == '__main__':
    print_inputs()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
