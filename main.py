# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#Breaks up a given string with split()
def breakUp1(str):
    new = str.split()
    for i in new:
        print(i)

#Breaks up a given string without split()
def breakUp2(str):
    list = []
    temp = ""
    #Break up the string into a list
    for i in str:
        if i == " ":
            list.append(temp)
            temp = ""
        else:
            temp += i
    if temp:
        list.append(temp)

    #Print the string
    for k in list:
        print(k)

# Main code execution
if __name__ == '__main__':
    string=input("Enter a string:")
    breakUp1(string)
    breakUp2(string)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
