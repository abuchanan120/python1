# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random

def random_avg():
    sum = 0
    for i in range(10):
        sum += random.randint(0,1000)
    print("The average of 10 random integers from 0-1000:", sum/10)

# Main code execution
if __name__ == '__main__':
    random_avg()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
