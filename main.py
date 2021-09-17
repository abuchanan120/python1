# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def print_inputs():
    print("What is your name?")
    name=input()
    print("Your name is:",name)

    print("Enter a number:")
    number=int(input())
    print(number, " multiplied by ",number,"= ",number * number,sep="")

    print("Enter a word:")
    word=input()
    print("Number of letters in ",word,": ",word.__len__(),sep="")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_inputs()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
