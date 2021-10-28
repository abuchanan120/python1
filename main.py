# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys



# Main code execution
if __name__ == '__main__':
    print(f"Arguments Count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
